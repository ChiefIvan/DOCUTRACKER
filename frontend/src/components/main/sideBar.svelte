<script>
  import { backendAddress } from "../../stores";

  import Auth from "../entries/auth.svelte";

  let authBind;

  const logoutAddress = `${backendAddress}/logout`;
  const errorMessage = "";

  const handleLogout = () => {
    authBind.getEndPoint(logoutAddress, errorMessage, {
      Authorization: `Bearer ${localStorage.getItem("remembered") || ""}`,
    });

    localStorage.setItem("remembered", "")
  };
</script>

<Auth bind:this={authBind} />

<section>
  <nav>Hello Sidebar</nav>
  <button on:click={handleLogout}>Logout</button>
</section>

<style>
  section {
    position: sticky;
    top: 0;
    left: 0;
    z-index: 2;

    display: flex;
    justify-content: center;
    align-items: center;

    min-width: 15rem;
    height: 100vh;
    background-color: #333;
    color: white;

    & nav {
      width: calc(15rem * 0.9);
      height: calc(100vh * 0.97);
    }
  }
</style>
