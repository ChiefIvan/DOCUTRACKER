<script lang="ts">
  import CheckAuthenticity from "../shared/CheckAuthenticity.svelte";
  export let authToken = "";
</script>

<svelte:head>
  <title>DOCUTRACKER | History</title>
</svelte:head>

<CheckAuthenticity {authToken} on:user></CheckAuthenticity>
<main>Hello From History</main>
