<script lang="ts">
  import { useLocation } from "svelte-routing";
  import { location } from "../../store";
  import type { RouteLocation } from "svelte-routing/types/Route";
  import type { Readable } from "svelte/store";

  const userLocation: Readable<RouteLocation> = useLocation();
  $: $location = $userLocation.pathname;
</script>
