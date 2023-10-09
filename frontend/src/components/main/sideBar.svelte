<script>
  import { backendAddress } from "../../stores";
  import { fade } from "svelte/transition";

  import Auth from "../entries/auth.svelte";
  import ArrowIcon from "../assets/arrowIcon.svelte";
  import Button from "../entries/button.svelte";
  import Logouticon from "../assets/logoutIcon.svelte";
  import LogoutIcon from "../assets/logoutIcon.svelte";

  let authBind;
  let shrink = false;
  let arrowState = false;

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

  const handleState = () => {
    shrink = !shrink;
    arrowState = !arrowState;
  };
</script>

<Auth bind:this={authBind} />

<section class:on-shrink={shrink}>
  <nav>
    <!-- {#if shrink}
      <ul>
        <p>SVG's goes heres</p>
      </ul>
    {:else}
      Hello
    {/if} -->
    Hello
  </nav>
  <div>
    <div class="end-wrapper">
      {#if shrink}
        <div class="nav-wrapper" class:on-shrink={shrink}>
          <LogoutIcon on:click={handleLogout} />
        </div>
      {:else}
        <div class="nav-wrapper">
          <Button
            btnName={"Logout"}
            btnLoginSize={true}
            btnTitle={"Logout"}
            onhover={true}
            on:click={handleLogout}
          />
        </div>
      {/if}
    </div>
    <div class="end-wrapper">
      <ArrowIcon on:click={handleState} {arrowState} />
    </div>
  </div>
</section>

<style>
  section {
    position: sticky;
    top: 0;
    left: 0;
    padding: 0 calc(var(--size-5) * 0.3);

    display: flex;
    flex-direction: column;

    width: 15rem;
    height: 100vh;
    background-color: #333;
    color: white;
    transition: all ease-in-out var(--dur);
    overflow: hidden;

    & nav {
      width: 100%;
      height: 100%;

      & ul {
        display: flex;
        flex-direction: column;
        align-items: center;
      }
    }

    & div.end-wrapper {
      width: 100%;
      transition: all ease-in-out var(--dur);
      padding: var(--size-6) 0;
      margin: calc(var(--size-6) * 0.8) 0;
      display: flex;
      justify-content: center;
      align-items: flex-end;
      flex-direction: column;
      position: relative;

      & div.nav-wrapper {
        position: absolute;
        inset: 0;
        display: flex;
        align-items: center;
      }

      & div.on-shrink {
        justify-content: center;
      }
    }
  }

  section.on-shrink {
    width: var(--size-3);
  }
</style>
