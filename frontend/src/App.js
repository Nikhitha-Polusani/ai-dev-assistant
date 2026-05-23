import { useEffect, useRef } from "react";
import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);


  const sendMessage = async () => {
  if (!message.trim()) return;

  const userMsg = { type: "user", text: message };
  setChat((prev) => [...prev, userMsg]);

  // ✅ show typing indicator
  const typingMsg = { type: "bot", text: "AI is typing..." };
  setChat((prev) => [...prev, typingMsg]);

  try {
    const response = await axios.post("http://127.0.0.1:8000/chat", {
      message: message,
    });

    // ✅ remove typing message
    setChat((prev) => prev.slice(0, -1));

    // ✅ type response slowly (animation)
    let text = response.data.response;
    let current = "";

    for (let i = 0; i < text.length; i++) {
      await new Promise((resolve) => setTimeout(resolve, 20));
      current += text[i];
      setChat((prev) => [
        ...prev.slice(0, -1),
        { type: "bot", text: current },
      ]);
    }

  } catch (error) {
    console.error(error);
  }

  setMessage("");
};

  return (
    <div className="app">
      <h1>🤖 AI Assistant</h1>

      <div className="chat-box">
        {chat.map((msg, index) => (
          <div
            key={index}
            className={msg.type === "user" ? "message user" : "message bot"}
          >
            {msg.text}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>

      <div className="input-box">
        <input
  value={message}
  onChange={(e) => setMessage(e.target.value)}
  onKeyDown={(e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  }}
  placeholder="Ask something..."
/>
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
