<script lang="ts">
  import { fade } from "svelte/transition";
  import {
    navExpand,
    address,
    dark,
    handleFetch,
    type RequestAPI,
  } from "../../store";
  import { tooltip } from "../shared/Tooltip";

  import logoSimple from "../../assets/transparent-favicons-simple.png";
  import ArrowIcon from "../icons/ArrowIcon.svelte";
  import Button from "../shared/Button.svelte";
  import LogoutIcon from "../icons/LogoutIcon.svelte";
  import MediaQuery from "../shared/MediaQuery.svelte";
  import Navigation from "./Navigation.svelte";

  const logoutAddress = `${address}/logout`;
  const logoutMethod = "GET";

  const logoutRequest: RequestAPI = {
    method: logoutMethod,
    address: logoutAddress,
  };

  const handleExpand = () => {
    $navExpand = !$navExpand;
  };

  const handleLogout = async () => {
    const token = sessionStorage.getItem("remember");
    await handleFetch(logoutRequest, token);
    sessionStorage.removeItem("remember");
    window.location.href = "http://localhost:5173/";
  };
</script>

<div class="sidebar-section">
  <div class="sidebar" class:isExpanded={$navExpand} class:dark={$dark}>
    <div class="sidebar-wrapper">
      <div class="logo-wrapper" class:dark={$dark}>
        <img class="logo" src={logoSimple} alt="Docutracker's Logo" />
        {#if $navExpand}
          <h1
            transition:fade={{ duration: 200, delay: 200 }}
            class="title-name"
            class:dark={$dark}
          >
            DOCUTRACKER
          </h1>
        {/if}
      </div>
      <div class="navigation-wrapper">
        <Navigation />
      </div>
      <MediaQuery query="(min-width: 500px)" let:matches>
        {#if matches}
          <div class="logout-expand-wrapper">
            <div class="logout-wrapper">
              {#if $navExpand}
                <Button on:click={handleLogout}>Logout</Button>
              {:else}
                <LogoutIcon on:click={handleLogout} />
              {/if}
            </div>
            <ArrowIcon
              sizeMedium={true}
              arrowState={$navExpand}
              dark={$dark}
              on:click={handleExpand}
            />
          </div>
        {/if}
      </MediaQuery>
    </div>
  </div>
</div>
{#if $navExpand}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div
    on:click={() => ($navExpand = !$navExpand)}
    transition:fade={{ duration: 200, delay: 200 }}
    class="overlap"
  />
{/if}

<style>
  div.sidebar-section {
    & div.sidebar {
      position: sticky;
      transition: all ease-in-out 500ms;
      top: 0;
      left: 0;
      height: 100vh;
      width: 3.4rem;
      z-index: 4;
      overflow: hidden;
      background-color: var(--main-col-5);

      & div.sidebar-wrapper {
        margin: 0 0.7rem;
        position: relative;
        height: 100%;

        & div.logo-wrapper {
          background-color: var(--main-col-5);

          display: flex;
          align-items: center;
          column-gap: 0.8rem;
          border-bottom: 1px solid var(--main-col-7);
          padding: 0.12rem 0;
          text-align: center;
          transition: all ease-in-out 500ms;

          & img.logo {
            max-width: 2.1rem;
          }

          & h1.title-name {
            transition: color ease-in-out 500ms;
            font-size: 1.2rem;
            font-weight: 700;
            letter-spacing: -0.05rem;
            color: var(--scroll-color);
          }

          & h1.dark {
            color: var(--background);
          }
        }

        & div.dark {
          border-bottom-color: var(--input-color);
          background-color: var(--dark-main-col-5);
        }

        & div.navigation-wrapper {
          /* height: 100%; */
        }

        & div.logout-expand-wrapper {
          position: absolute;
          bottom: 0;
          width: 100%;
          text-align: end;

          & div.logout-wrapper {
            height: 2rem;
            position: relative;
          }
        }

        & div.logout-expand-wrapper > * {
          margin-bottom: 0.5rem;
        }
      }
    }

    & div.isExpanded {
      width: 15rem;
    }

    & div.dark {
      background-color: var(--dark-main-col-5);
    }
  }

  @media (max-width: 900px) {
    div.sidebar-section
      div.sidebar
      div.sidebar-wrapper
      div.logo-wrapper
      h1.title-name {
      font-size: 1.1rem;
    }
  }

  @media (max-width: 500px) {
    div.sidebar-section div.sidebar {
      position: fixed;
      width: 0;
      z-index: 5;
    }

    div.sidebar-section div.isExpanded {
      width: 14rem;
    }

    div.overlap {
      transition: background-color ease-in-out 300ms;
      position: fixed;
      background-color: rgba(0, 0, 0, 0.6);
      z-index: 4;
      inset: 0;
    }
  }
</style>
