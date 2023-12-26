require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.19",
  paths: {
    artifacts: './src/artifacts',
  },
  networks: {
    localhost: {
      hardhat: true,
      url: "http://localhost:8545",
    },
    hardhat: {
      chainId: 1337,
      
    },

  }
};
