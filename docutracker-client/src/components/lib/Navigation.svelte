<script lang="ts">
  import DashboardLogo from "../icons/DashboardLogo.svelte";
</script>

<div class="navigation-wrapper-sidebar">
  <div class="navigation">
    <div class="navigation-selection">
      <DashboardLogo />
      <span>Dashboard</span>
    </div>
  </div>
</div>

<style>
  div.navigation-wrapper-sidebar {
    margin-top: 5rem;

    & div.navigation {
      transition: all ease-in-out 300ms;
      border-radius: 1rem;

      & div.navigation-selection {
        display: flex;
        align-items: center;
      }
    }

    & div.navigation:hover {
      background-color: var(--header-color);
    }
  }
</style>
