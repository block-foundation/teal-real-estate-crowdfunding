

from pyteal import *

def crowdfunding_campaign(goal, deadline, beneficiary):

    def predicate(txn: Txn, gtxn: Gtxn, global_: Global, local: LocalStateSchema) -> Expr:
        on_initialization = And(
            Txn.application_id() == Int(0),
            Txn.global_num_byte_slices() == Int(0),
            Txn.global_num_uints() == Int(0)
        )

        on_contribution = And(
            Txn.application_id() != Int(0),
            Txn.close_remainder_to() == beneficiary,
            Txn.amount() < goal,
            Global.latest_timestamp() < deadline
        )

        on_withdraw = And(
            Txn.application_id() != Int(0),
            Txn.sender() == beneficiary,
            Global.latest_timestamp() >= deadline,
            Global.asset_holding_balance(Txn.xfer_asset()).value() >= goal
        )

        return Or(on_initialization, on_contribution, on_withdraw)

    return compileTeal(predicate, mode=Mode.Signature, version=4)
