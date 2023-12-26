# UAS SKD SIMPLE SMART CONTRACT  

## Laila Ainur Rahma (V3922026)



### LANGKAH LANGKAH

#### 1. npx create-react-app uasskd
![npx create react ](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/create%20react%20app.png?raw=true)
#### 2. npm i hardhat --save-dev
#### 3. npx hardhat init
![hardhat init](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/install%20hardhat%20%20%26%20hardhat%20innit.png?raw=true)
#### 4. Tulis script 

##### contracts/Greeter.sol
``` Solidity
//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "hardhat/console.sol";

contract Greeter {
    string private greeting;

    constructor(string memory _greeting) {
        console.log("Deploying a Greeter with greeting:", _greeting);
        greeting = _greeting;
    }

function greet() public view returns (string memory) {
    console.log("Entering greet function");
    // ... rest of the code ...
    console.log("Exiting greet function");
    return greeting;
}


    function setGreeting(string memory _greeting) public {
        console.log("Changing greeting from '%s' to '%s'", greeting, _greeting);
        greeting = _greeting;
    }
}



```
##### script/Deploy.js
``` Javascript
const hre = require("hardhat");

async function main() {
  const Greeter = await hre.ethers.getContractFactory("Greeter");
  const greeter = await Greeter.deploy("Hello, Hardhat! It's Lala's Project for UAS SKD");



  console.log("Greeter deployed to:", greeter.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

```
#### 5. npx hardhat compile (untuk mengcompile solidity)
#### 6. npx hardhat node
![npx  hardhat node ](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/hardhat%20node.png?raw=true)
#### 7. buat interface react
![int react ](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/interface.png?raw=true)
#### 8. jika fetch greeting maka akan menampilkan greeting yang tekah dibuat
![fetch ](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/fetch%20greeting.png?raw=true)

#### 7. jika set greeting maaka akan masuk ke akun metamask dan menampilkan transaksi
![set](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/set%20greeting.png?raw=true)
![metamask](https://github.com/laainra/UAS-SKD-V3922026-LAILA-AINUR-R/blob/main/Screenshot/metamask.png?raw=true)
