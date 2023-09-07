<script>
  import { serverResponse } from "../../stores";

  const logoutAPI = "http://127.0.0.1:5000/logout";

  const hanleLogout = () => {
    fetch(logoutAPI)
      .then((response) => response.json())
      .then((data) => ($serverResponse = data))
      .catch((error) => console.error("Error:", error));
  };
</script>

<button on:click={hanleLogout}> Logout </button>
