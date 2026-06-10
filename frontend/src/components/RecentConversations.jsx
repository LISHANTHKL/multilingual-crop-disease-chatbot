import { useEffect, useState } from "react";
import { getRecentChats } from "../services/chatService";

export default function RecentConversations() {

  const [chats, setChats] = useState([]);

  useEffect(() => {

    const loadChats = async () => {

      try {

        const data = await getRecentChats();

        setChats(data.data);

      } catch (error) {

        console.error(error);

      }

    };

    loadChats();

  }, []);

  return (
    <div className="weather-card p-4">

      <h4 className="mb-4">
        Recent Conversations
      </h4>

      {
        chats.length === 0
        ? (
          <p>No Chats Available</p>
        )
        : (
          chats.map((chat) => (

            <div
              key={chat._id}
              className="alert alert-dark"
            >
              {chat.message}
            </div>

          ))
        )
      }

    </div>
  );
}