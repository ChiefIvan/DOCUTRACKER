<script>
  import axios from "axios";

  async function logout() {
    try {
      await axios.post("http://127.0.0.1:5000/index");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  }
</script>

<button on:click={logout}> Logout </button>
