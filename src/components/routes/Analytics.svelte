<script lang="ts">
  import CheckAuthenticity from "../shared/CheckAuthenticity.svelte";
  export let authToken = "";
</script>

<svelte:head>
  <title>DOCUTRACKER | Analytics</title>
</svelte:head>

<CheckAuthenticity {authToken} on:user></CheckAuthenticity>
<main>Hello From Analytics</main>
