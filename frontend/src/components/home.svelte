<script>
  import { userContent } from "../stores";
  import { onMount } from "svelte";
  import Auth from "./entries/auth.svelte";

  const homeAddress = "http://127.0.0.1:5000/index";
  const homeMethod = "GET";
  const homeErrMsg = "Token is Expired or Invalid Token, Please Login Again!";

  let isMounted = false;
  let userId = "";

  onMount(() => {
    userId = localStorage.getItem("remembered") || "";
    isMounted = true;
  });
</script>

{#if isMounted}
  <Auth
    apiAddress={homeAddress}
    authMethod={homeMethod}
    authData={userId}
    errorMessage={homeErrMsg}
  />
{/if}
<main>
  {#if Object.keys($userContent).length != 0}
    <h1>Currently logged in as:</h1>
    <h2>{$userContent["email"]}</h2>
    <p>ID: {$userContent["id"]}, Username: {$userContent["user_name"]}</p>
    <p>Token: {$userContent["token"]}</p>
  {/if}
</main>

<style>
  main {
    text-align: center;
  }
</style>
