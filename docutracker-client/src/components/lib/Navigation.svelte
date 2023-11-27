<script lang="ts">
  import { navExpand, location } from "../../store";
  import { navigate } from "svelte-routing";
  import { fade } from "svelte/transition";

  import ActivityIcon from "../icons/ActivityIcon.svelte";
  import DashboardLogo from "../icons/DashboardLogo.svelte";
  import ScanIcon from "../icons/ScanIcon.svelte";
  import AddIcon from "../icons/AddIcon.svelte";

  const goToDashboard = () => {
    navigate("/dashboard");
  };

  const goToUpdates = () => {
    navigate("/updates");
  };

  const navigation = [
    {
      id: 1,
      navName: "Dashboard",
      comp: DashboardLogo,
      location: "/dashboard",
      bind: goToDashboard,
    },
    {
      id: 2,
      navName: "Updates",
      comp: ActivityIcon,
      location: "/updates",
      bind: goToUpdates,
    },
  ];

  console.log($location);
</script>

<div class="navigation-wrapper-sidebar">
  {#if $navExpand}
    <span class="shortcut-label" transition:fade={{ duration: 200, delay: 200 }}
      >Shortcuts</span
    >
  {/if}
  <div class="shortcuts">
    <div class="shortcut-links">
      <ScanIcon></ScanIcon>
      {#if $navExpand}
        <span
          transition:fade={{ duration: 200, delay: 200 }}
          class="shortcut-name">Scan Document</span
        >
      {/if}
    </div>
    <div class="shortcut-links">
      <AddIcon></AddIcon>
      {#if $navExpand}
        <span
          transition:fade={{ duration: 200, delay: 200 }}
          class="shortcut-name">Register Document</span
        >
      {/if}
    </div>
  </div>
  {#if $navExpand}
    <div transition:fade={{ duration: 200, delay: 200 }} class="navigation">
      {#each navigation as value (value.id)}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div
          on:click={value.bind}
          class="navigation-selection"
          class:active={value.location === $location && true}
        >
          <svelte:component
            this={value.comp}
            compColor={value.location === $location && true}
          ></svelte:component>
          <span class:active={value.location === $location && true}
            >{value.navName}</span
          >
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  div.navigation-wrapper-sidebar {
    & span.shortcut-label {
      margin: 0.5rem 0;
      display: inline-block;
    }

    & div.shortcuts {
      & div.shortcut-links {
        transition: border-bottom-color ease-in-out 300ms;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        border-bottom: 1px solid transparent;
        margin: 0.5rem 0;
        padding-bottom: 0.2rem;
        cursor: pointer;

        & span.shortcut-name {
          font-size: 1rem;
          color: var(--scroll-color);
        }
      }

      & div.shortcut-links:hover {
        border-bottom-color: var(--header-color);
      }
    }

    & div.navigation {
      border-radius: 0.5rem;
      overflow: hidden;
      border: 1px solid var(--header-color);
      margin-top: 2rem;

      & div.navigation-selection {
        transition: all ease-in-out 300ms;
        cursor: pointer;
        display: flex;
        align-items: center;
        column-gap: 0.1rem;
        padding-left: 1rem;
        height: 2.5rem;
      }

      & div.navigation-selection:hover {
        background-color: var(--header-color);
      }

      & div.active {
        background-color: var(--component-active);
      }

      & span {
        color: var(--scroll-color);
        margin-left: 0.5rem;
        font-size: 1rem;
      }

      & span.active {
        color: var(--icon-active-color);
      }
    }
  }
</style>
