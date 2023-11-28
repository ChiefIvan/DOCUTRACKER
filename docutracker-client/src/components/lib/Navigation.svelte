<script lang="ts">
  import { navExpand, location } from "../../store";
  import { navigate } from "svelte-routing";
  import { fade } from "svelte/transition";

  import ActivityIcon from "../icons/ActivityIcon.svelte";
  import DashboardLogo from "../icons/DashboardLogo.svelte";
  import ScanIcon from "../icons/ScanIcon.svelte";
  import AddIcon from "../icons/AddIcon.svelte";
  import BellIcon from "../icons/BellIcon.svelte";
  import RouteIcon from "../icons/RouteIcon.svelte";
  import UpdateRouteIcon from "../icons/UpdateRouteIcon.svelte";
  import AnalyticsIcon from "../icons/AnalyticsIcon.svelte";
  import OverviewIcon from "../icons/OverviewIcon.svelte";

  const goToDashboard = () => {
    navigate("/dashboard");
  };

  const goToUpdates = () => {
    navigate("/updates");
  };

  const goToNotifications = () => {
    navigate("/notifications");
  };

  const goToAnalytics = () => {
    navigate("/analytics");
  };

  const goToOverview = () => {
    navigate("/document/overview");
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
      navName: "Notifications",
      comp: BellIcon,
      location: "/notifications",
      bind: goToNotifications,
    },
    {
      id: 3,
      navName: "History",
      comp: ActivityIcon,
      location: "/updates",
      bind: goToUpdates,
    },
    {
      id: 4,
      navName: "Analytics",
      comp: AnalyticsIcon,
      location: "/analytics",
      bind: goToAnalytics,
    },
    {
      id: 5,
      navName: "Overview",
      comp: OverviewIcon,
      location: "/document/overview",
      bind: goToOverview,
    },
  ];

  const shortcut = [
    {
      id: 1,
      shortcutName: "Scan Document",
      comp: ScanIcon,
      location: "",
      bind: "",
    },
    {
      id: 2,
      shortcutName: "Register Document",
      comp: AddIcon,
      location: "",
      bind: "",
    },
    {
      id: 3,
      shortcutName: "Register Route",
      comp: RouteIcon,
      location: "",
      bind: "",
    },
    {
      id: 4,
      shortcutName: "Update Route",
      comp: UpdateRouteIcon,
      location: "",
      bind: "",
    },
  ];
</script>

<div class="navigation-wrapper-sidebar">
  {#if $navExpand}
    <span class="shortcut-label" transition:fade={{ duration: 200, delay: 200 }}
      >Shortcuts</span
    >
  {/if}
  <div class="shortcuts">
    {#each shortcut as value (value.id)}
      <div class="shortcut-links">
        <svelte:component this={value.comp}></svelte:component>
        {#if $navExpand}
          <span
            transition:fade={{ duration: 200, delay: 200 }}
            class="shortcut-name">{value.shortcutName}</span
          >
        {/if}
      </div>
    {/each}
  </div>
  {#if $navExpand}
    <span class="shortcut-label" transition:fade={{ duration: 200, delay: 200 }}
      >Navigation</span
    >
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
            medium={value.navName === "Notifications"}
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
  span.shortcut-label {
    margin-top: 2rem;
    margin-bottom: 1rem;
    display: inline-block;
    color: var(--scroll-color);
    font-weight: bold;
  }

  div.navigation-wrapper-sidebar {
    & div.shortcuts {
      & div.shortcut-links {
        transition: border-bottom-color ease-in-out 300ms;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        border-bottom: 1px solid transparent;
        margin: 0.2rem 0;
        padding-bottom: 0.2rem;
        cursor: pointer;

        & span.shortcut-name {
          font-size: 0.9rem;
          color: var(--scroll-color);
          display: inline-block;
          text-wrap: nowrap;
        }
      }

      & div.shortcut-links:hover {
        border-bottom-color: var(--header-color);
      }
    }

    & div.navigation {
      border-radius: 1rem;
      overflow: hidden;
      border: 1px solid var(--header-color);

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
