import { useState } from "react";
import { ethers } from 'ethers';
import { Web3Provider } from '@ethersproject/providers';
import Greeter from "./artifacts/contracts/Greeter.sol/Greeter.json";
import "./App.css";

// The contract address
const greeterAddress = "0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266";

function App() {
  // Property Variables

  const [message, setMessage] = useState("");
  const [currentGreeting, setCurrentGreeting] = useState("");

  // Helper Functions

  // Requests access to the user's MetaMask Account
  // https://metamask.io/
  async function requestAccount() {
    await window.ethereum.request({ method: "eth_requestAccounts" });
  }

  // Fetches the current value stored in greeting
  async function fetchGreeting() {
    // If MetaMask exists
    if (typeof window.ethereum !== "undefined") {
      const provider = new Web3Provider(window.ethereum);
      const contract = new ethers.Contract(
        greeterAddress,
        Greeter.abi,
        provider
      );
      try {
        // Call Greeter.greet() and display the current greeting in the `console`
        const data = await contract.greet();
        console.log("data: ", data);
        setCurrentGreeting(data);
      } catch (error) {
        console.log("Error: ", error);
      }
    }
  }

  // Sets the greeting from the input text box
  async function setGreeting() {
    if (!message) return;

    // If MetaMask exists
    if (typeof window.ethereum !== "undefined") {
      await requestAccount();

      const provider = new Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      // Create contract with signer
      const contract = new ethers.Contract(greeterAddress, Greeter.abi, signer);
      const transaction = await contract.setGreeting(message);

      setMessage("");
      await transaction.wait();
      fetchGreeting();
    }
  }

  // Return
  return (
    <div className="App">
      <div className="App-header">
        {/* DESCRIPTION  */}
        <div className="description">
          <h1>UAS SKD</h1>
          <h3>Syahla Chandra Ramadhania -V3922042</h3>
        </div>
        {/* BUTTONS - Fetch and Set */}
        <div className="custom-buttons">
          <button onClick={fetchGreeting} style={{ backgroundColor: "green" }}>
            Fetch Greeting
          </button>
          <button onClick={setGreeting} style={{ backgroundColor: "red" }}>
            Set Greeting
          </button>
        </div>
        {/* INPUT TEXT - String  */}
        <input
          onChange={(e) => setMessage(e.target.value)}
          value={message}
          placeholder="Set Greeting Message"
        />

        {/* Current Value stored on Blockchain */}
        <h2 className="greeting">Greeting: {currentGreeting}</h2>
      </div>
    </div>
  );
}

export default App;
