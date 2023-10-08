<script>
  import { backendAddress } from "../../stores";

  import Auth from "../entries/auth.svelte";

  let authBind;
  let shrink = false;

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

<section class:on-shrink={shrink}>
  <nav>
    Hello Sidebar
    <button on:click={handleLogout}>Logout</button>
    <button on:click={() => (shrink = !shrink)}>Shrink</button>
  </nav>
</section>

<style>
  section {
    position: sticky;
    top: 0;
    left: 0;
    z-index: 2;

    display: flex;
    flex-direction: column;

    width: 15rem;
    height: 100vh;
    background-color: #333;
    color: white;
    transition: all ease-in-out var(--dur);
    overflow: hidden;
  }

  section.on-shrink {
    width: var(--size-3);
  }
</style>
