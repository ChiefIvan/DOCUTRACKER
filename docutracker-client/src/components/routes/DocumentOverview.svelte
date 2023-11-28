<script lang="ts">
  import CheckAuthenticity from "../shared/CheckAuthenticity.svelte";
  export let authToken = "";
</script>

<CheckAuthenticity {authToken} on:user></CheckAuthenticity>
<main>Hello From Document Overview</main>
