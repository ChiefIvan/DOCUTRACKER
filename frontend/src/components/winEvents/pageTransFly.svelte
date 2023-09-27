<script>
  import { fly } from "svelte/transition";
  import { useLocation } from "svelte-routing";
  import {
    pageTransitionValue1,
    pageTransitionValue2,
    location,
  } from "../../stores";

  const pageTransitionDuration = 200;
  const userLocation = useLocation();

  $: $location = $userLocation.pathname;
</script>

{#key $userLocation.pathname}
  <main
    in:fly={{
      x: $pageTransitionValue1,
      duration: pageTransitionDuration,
      delay: pageTransitionDuration + 100,
    }}
    out:fly={{ x: $pageTransitionValue2, duration: pageTransitionDuration }}
  >
    <slot />
  </main>
{/key}

<style>
  main {
    display: grid;
    grid-template-rows: 1fr;
    grid-template-columns: 1fr;
  }

  main > :global(*) {
    grid-row: 1;
    grid-column: 1;
  }
</style>
