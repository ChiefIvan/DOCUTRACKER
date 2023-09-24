<script>
  import { userContent, serverResponse } from "../../stores";
  import { navigate } from "svelte-routing";

  export let apiAddress = "";
  export let authData = "";
  export let authMethod = "";
  export let errorMessage = "";

  let headers =
    authData !== "POST"
      ? { Authorization: `Bearer ${authData}` }
      : { "Content-Type": "application/json" };

  fetch(apiAddress, {
    method: authMethod,
    headers: headers,
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
      $serverResponse = { error: errorMessage };
      navigate("/login");
    });
</script>
