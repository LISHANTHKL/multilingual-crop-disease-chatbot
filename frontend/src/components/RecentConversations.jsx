import {
  useEffect,
  useState
} from "react";

import {
  getRecentConversations
} from "../services/dashboardService";

export default function RecentConversations() {

  const [conversations,
    setConversations] = useState([]);

  useEffect(() => {

    loadConversations();

  }, []);

  const loadConversations =
    async () => {

      try {

        const data =
          await getRecentConversations();

        setConversations(
          data.conversations
        );

      } catch (error) {

        console.error(error);

      }
    };

  return (

    <div className="card shadow-sm">

      <div className="card-header">

        <h5 className="mb-0">
          Recent Conversations
        </h5>

      </div>

      <div className="card-body">

        {
          conversations.length === 0 ? (

            <p>
              No conversations found
            </p>

          ) : (

            conversations.map(
              (
                chat,
                index
              ) => (

                <div
                  key={index}
                  className="
                    border-bottom
                    mb-3
                    pb-2
                  "
                >

                  <strong>
                    {chat.user_id}
                  </strong>

                  <p className="mb-1">
                    {chat.query}
                  </p>

                  <small
                    className="
                      text-muted
                    "
                  >
                    Crop:
                    {" "}
                    {chat.crop || "N/A"}
                  </small>

                  <br />

                  <small
                    className="
                      text-muted
                    "
                  >
                    Disease:
                    {" "}
                    {chat.disease || "N/A"}
                  </small>

                </div>

              )
            )

          )
        }

      </div>

    </div>

  );
}

