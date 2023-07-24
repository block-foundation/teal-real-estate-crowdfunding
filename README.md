<div align="right">

  [![license](https://img.shields.io/github/license/block-foundation/teal-real-estate-crowdfunding?color=green&label=license&style=flat-square)](LICENSE.md)
  ![stars](https://img.shields.io/github/stars/block-foundation/teal-real-estate-crowdfunding?color=blue&label=stars&style=flat-square)
  ![contributors](https://img.shields.io/github/contributors/block-foundation/teal-real-estate-crowdfunding?color=blue&label=contributors&style=flat-square)

</div>

---

<div>
    <img align="right" src="https://raw.githubusercontent.com/block-foundation/brand/master/logo/logo_gray.png" width="96" alt="Block Foundation Logo">
    <h1 align="left">Real-Estate Crowdfunding</h1>
    <h3 align="left">Block Foundation Smart Contract Series [Teal]</h3>
</div>

---

<div>
<img align="right" width="75%" src="https://raw.githubusercontent.com/block-foundation/brand/master/image/repository_cover/block_foundation-structure-03-accent.jpg"  alt="Block Foundation">
<br>
<details open="open">
<summary>Table of Contents</summary>
  
- [Introduction](#style-guide)
- [Quick Start](#quick-start)
- [Contract](#contract)
- [Development Resources](#development-resources)
- [Legal Information](#legal-information)
  - [Copyright](#copyright)
  - [License](#license)
  - [Warning](#warning)
  - [Disclaimer](#disclaimer)

</details>
</div>

<br clear="both"/>

## Introduction

Introducing the Real Estate Crowdfunding Blockchain Solution

As technology continues to evolve and reshape industries globally, we are excited to bring you our latest development: a groundbreaking solution for the real estate industry. This innovative project applies the principles of blockchain technology to real estate crowdfunding, a venture we believe will revolutionize how individuals and organizations raise funds for real estate projects.

Our solution utilizes Smart Contract technology to facilitate, validate, and enforce negotiation or performance of an agreement. This automated, self-executing contract with the terms of the agreement directly written into code enables the democratization of real estate funding, rendering it more transparent, efficient, and accessible.

The Smart Contract has been designed with several features to enhance functionality and security. First, users can create a new crowdfunding campaign, specifying a goal amount to raise. Then, interested investors can contribute to the campaign while the contract keeps track of each investor's contribution and the total raised amount.

Moreover, the contract also has built-in mechanisms to safeguard the interests of both project creators and investors. For instance, if a crowdfunding campaign does not reach its funding goal by the specified deadline, the contract will automatically facilitate refunds to the investors.

This Blockchain-based Real Estate Crowdfunding solution signifies a step forward in the digital transformation of the real estate industry. It brings us one step closer to a decentralized financial landscape where anyone can participate in investment opportunities that were traditionally limited to institutions or the wealthy.

Join us on this journey to disrupt and democratize real estate crowdfunding, making it transparent, secure, and accessible to all.

## Quick Start


## Contract

This PyTeal contract checks three conditions:

- Initialization of the contract.
- Contribution to the contract (can't exceed the goal, must be done before the deadline).
- Withdrawal from the contract (can only be done by the beneficiary and only after the deadline if the goal has been met).
- Keep in mind, unlike Ethereum, Algorand doesn’t automatically track the balance of an account in a contract, you would need to handle it off-chain or use Algorand Standard Assets (ASA) as a - workaround.

Remember that PyTeal (and Algorand in general) does not have the same capabilities as Solidity (and Ethereum), and therefore you may need to change your approach or use different features when working with it. Always consult with a knowledgeable developer or team when implementing smart contracts to ensure that they are secure and function as expected.

## Development Resources

### Other Repositories

#### Block Foundation Smart Contract Series

|                                   | `Solidity`  | `Teal`      |
| --------------------------------- | ----------- | ----------- |
| **Template**                      | [**>>>**](https://github.com/block-foundation/solidity-template) | [**>>>**](https://github.com/block-foundation/teal-template) |
| **Architectural Design**          | [**>>>**](https://github.com/block-foundation/solidity-architectural-design) | [**>>>**](https://github.com/block-foundation/teal-architectural-design) |
| **Architecture Competition**      | [**>>>**](https://github.com/block-foundation/solidity-architecture-competition) | [**>>>**](https://github.com/block-foundation/teal-architecture-competition) |
| **Housing Cooporative**           | [**>>>**](https://github.com/block-foundation/solidity-housing-cooperative) | [**>>>**](https://github.com/block-foundation/teal-housing-cooperative) |
| **Land Registry**                 | [**>>>**](https://github.com/block-foundation/solidity-land-registry) | [**>>>**](https://github.com/block-foundation/teal-land-registry) |
| **Real-Estate Crowdfunding**      | [**>>>**](https://github.com/block-foundation/solidity-real-estate-crowdfunding) | [**>>>**](https://github.com/block-foundation/teal-real-estate-crowdfunding) |
| **Rent-to-Own**                   | [**>>>**](https://github.com/block-foundation/solidity-rent-to-own) | [**>>>**](https://github.com/block-foundation/teal-rent-to-own) |
| **Self-Owning Building**          | [**>>>**](https://github.com/block-foundation/solidity-self-owning-building) | [**>>>**](https://github.com/block-foundation/teal-self-owning-building) |
| **Smart Home**                    | [**>>>**](https://github.com/block-foundation/solidity-smart-home) | [**>>>**](https://github.com/block-foundation/teal-smart-home) |

## Legal Information

### Copyright

Copyright 2023, [Stichting Block Foundation](https://www.blockfoundation.io). All rights reserved.

### License

Except as otherwise noted, the content in this repository is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/), and
code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).

Also see [LICENSE](https://github.com/block-foundation/community/blob/master/LICENSE) and [LICENSE-CODE](https://github.com/block-foundation/community/blob/master/LICENSE-CODE).

### Warning

**Please note that this code should be audited by a professional smart-contract auditor before being used in a production environment as it is a simplified example and may not cover all potential security vulnerabilities.**

### Disclaimer

**THIS SOFTWARE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.**
