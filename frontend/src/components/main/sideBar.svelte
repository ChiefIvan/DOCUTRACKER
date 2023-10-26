<script>
  import { backendAddress, dark } from "../../stores";
  import { navigate } from "svelte-routing";
  import { fade } from "svelte/transition";

  import Auth from "../entries/auth.svelte";
  import ArrowIcon from "../assets/arrowIcon.svelte";
  import Button from "../entries/button.svelte";
  import Logouticon from "../assets/logoutIcon.svelte";
  import LogoutIcon from "../assets/logoutIcon.svelte";
  import favicon from "../../lib/transparent-favicons-simple.png";

  let authBind;
  let shrink = false;
  let arrowState = false;

  const handleLogout = () => {
    const remembered = localStorage.getItem("remembered") || "";
    const logoutAddress = `${backendAddress}/logout`;
    const errorMessage = "";

    console.log(remembered);

    if (remembered.length !== 0) {
      authBind.getEndPoint(logoutAddress, errorMessage, {
        Authorization: `Bearer ${remembered}`,
      });
    }

    navigate("/");
    localStorage.setItem("remembered", "");
  };

  const handleState = () => {
    shrink = !shrink;
    arrowState = !arrowState;
  };
</script>

<Auth bind:this={authBind} />

<section class:on-shrink={shrink} class:dark={$dark}>
  <div class="logo-wrapper">
    <div class="start-wrapper" class:dark-mode={$dark}>
      <img src={favicon} alt="Docutracker's Logo" />
      {#if !shrink}
        <h2
          class="logo-name"
          class:dark-mode={$dark}
          transition:fade={{ duration: 200, delay: 200 }}
        >
          DOCUTRACKER
        </h2>
      {/if}
    </div>
  </div>
  <nav>
    <!-- {#if shrink}
      <ul>
        <p>SVG's goes heres</p>
      </ul>
    {:else}
      Hello
    {/if} -->
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
    z-index: 2;

    display: flex;
    flex-direction: column;

    width: 17rem;
    height: 100vh;
    background-color: var(--main-col-5);
    padding: 0 calc(var(--size-5) * 0.3);
    transition: all ease-in-out var(--dur);
    overflow: hidden;

    & div.logo-wrapper {
      position: relative;

      & div.start-wrapper {
        display: flex;
        align-items: center;
        column-gap: var(--size-6);

        border-bottom: 1px solid var(--main-col-6);
        height: var(--size-3);
        width: 100%;
        transition: all ease-in-out var(--dur);
        cursor: pointer;

        position: absolute;
        inset: 0;

        & img {
          max-width: calc(var(--size-3) * 0.7);
        }

        & h2.logo-name {
          font-size: 1.1rem;
          transition: all ease-in-out var(--dur);
          font-weight: 700;
          color: var(--main-col-3);
        }

        & h2.dark-mode {
          color: var(--bg);
        }
      }

      & div.dark-mode {
        border-bottom: 1px solid var(--scroll-col);
      }
    }

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

  section.dark {
    background-color: var(--dark-main-col-1);
  }

  section.on-shrink {
    width: var(--size-3);
  }
</style>
