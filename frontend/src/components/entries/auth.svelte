<script>
  import { fetchData, serverResponse } from "../../stores";
  import { navigate } from "svelte-routing";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  /**
   * @param {RequestInfo | URL} apiAddress
   * @param {any} errorMessage
   * @param {any} authHeader
   */
  export async function getEndPoint(apiAddress, errorMessage = "", authHeader) {
    await fetch(apiAddress, {
      method: "GET",
      headers: authHeader,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Server Unreachable");
        }

        return response.json();
      })

      .then((data) => (($fetchData = data), dispatch("authData", data)))
      .catch((error) => {
        console.error("Error:", error);
        if (errorMessage.length !== 0) {
          $serverResponse = { error: errorMessage };
        }
        navigate("/auth/u/login");
      });
  }

  /**
   * @param {RequestInfo | URL} apiAddress
   * @param {any} errorMessage
   * @param {any} authBody
   */
  export async function postEndPoint(
    apiAddress,
    errorMessage = "",
    authBody = {}
  ) {
    await fetch(apiAddress, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: authBody,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Server Unreachable");
        }

        return response.json();
      })

      .then((data) => ($fetchData = data))
      .catch((error) => {
        console.error("Error:", error);
        if (errorMessage.length !== 0) {
          $serverResponse = { error: errorMessage };
        }
        navigate("/auth/u/login");
      });
  }
</script>
