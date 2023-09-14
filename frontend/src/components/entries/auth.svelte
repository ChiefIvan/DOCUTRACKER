<script>
  import { userContent, serverResponse } from "../../stores";
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  const authAPI = "http://127.0.0.1:5000/index";
  onMount(() => {
    let user_token = localStorage.getItem("remembered") || "";

    if (user_token.length != 0) {
      fetch(authAPI, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${user_token}`,
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Logout request failed");
          }

          return response.json();
        })

        .then((data) => ($userContent = data))
        .catch((error) => {
          console.error("Error:", error);
          $serverResponse = { error: "Invalid Token! Please login again" };
          navigate("/login");
        });

      return;
    }

    navigate("/login");
  });
</script>
