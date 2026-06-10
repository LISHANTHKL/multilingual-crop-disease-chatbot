import { useEffect, useState } from "react";
import { getProfile } from "../services/profileService";

export default function UserProfileCard() {

  const [user, setUser] = useState(null);

  useEffect(() => {

    const loadProfile = async () => {

      try {

        const email =
          localStorage.getItem("userEmail");

        if (!email) {
          return;
        }

        const data =
          await getProfile(email);

        setUser(data.data);

      } catch (error) {

        console.error(
          "Profile Loading Error:",
          error
        );

      }

    };

    loadProfile();

  }, []);

  if (!user) {

    return (
      <div className="weather-card p-4">

        <h4>User Profile</h4>

        <p className="text-secondary">
          Loading profile...
        </p>

      </div>
    );

  }

  return (
    <div className="weather-card p-4">

      <div className="text-center">

        <img
          src={`https://ui-avatars.com/api/?name=${encodeURIComponent(
            user.full_name
          )}&background=16a34a&color=fff&size=128`}
          alt="profile"
          className="rounded-circle mb-3"
        />

        <h4>
          {user.full_name}
        </h4>

        <p className="text-success">
          Farmer
        </p>

      </div>

      <hr />

      <div className="mt-3">

        <p>
          <strong>Email:</strong>
          <br />
          {user.email}
        </p>

        <p>
          <strong>State:</strong>
          <br />
          {user.state || "Not Provided"}
        </p>

        <p>
          <strong>Language:</strong>
          <br />
          {user.preferred_language || "English"}
        </p>

      </div>

    </div>
  );
}
