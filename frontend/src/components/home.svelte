<script>
  import { fetchData, backendAddress } from "../stores";
  import { onMount } from "svelte";
  import Auth from "./entries/auth.svelte";

  const homeAddress = `${backendAddress}index`;
  const homeErrMsg = "Token is Expired or Invalid Token, Please Login Again!";

  let userId = "";
  let authBind;

  onMount(() => {
    userId = localStorage.getItem("remembered") || "";
    authBind.getEndPoint(homeAddress, homeErrMsg, {
      Authorization: `Bearer ${userId}`,
    });
  });
</script>

<Auth bind:this={authBind} />
<main>
  {#if Object.keys($fetchData).length != 0}
    <h1>Currently logged in as:</h1>
    <h2>{$fetchData["email"]}</h2>
    <p>ID: {$fetchData["id"]}, Username: {$fetchData["user_name"]}</p>
    <p>Token: {$fetchData["token"]}</p>
  {/if}
</main>

<style>
  main {
    text-align: center;
  }
</style>
