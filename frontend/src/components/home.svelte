<script>
  import { userContent } from "../stores";
  import Auth from "./entries/auth.svelte";
</script>

<Auth />
<main>
  {#if Object.keys($userContent).length != 0}
    <h1>Currently logged in as:</h1>
    <h2>{$userContent["email"]}</h2>
    <p>ID: {$userContent["id"]}, Username: {$userContent["user_name"]}</p>
  {/if}
</main>

<style>
  main {
    text-align: center;
  }
</style>
