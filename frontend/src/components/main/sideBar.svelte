<script>
  import { backendAddress } from "../../stores";

  import Auth from "../entries/auth.svelte";

  let authBind;
  const remembered = localStorage.getItem("remembered") || "";

  const logoutAddress = `${backendAddress}/logout`;
  const errorMessage = "";

  const handleLogout = () => {
    if (remembered.length !== 0) {
      authBind.getEndPoint(logoutAddress, errorMessage, {
        Authorization: `Bearer ${remembered}`,
      });
    }

    window.location.href = "/";
    localStorage.setItem("remembered", "");
  };
</script>

<Auth bind:this={authBind} />

<section>
  <nav>Hello Sidebar</nav>
  <div>
    <button on:click={handleLogout}>Logout</button>
  </div>
</section>

<style>
  section {
    position: sticky;
    top: 0;
    left: 0;
    z-index: 2;

    display: flex;
    flex-direction: column;

    min-width: 15rem;
    height: 100vh;
    background-color: #333;
    color: white;

    & nav {
      width: calc(15rem * 0.9);
      height: calc(100vh * 0.97);
      flex: 4;
    }

    & div {
      flex: 1;
    }
  }
</style>
