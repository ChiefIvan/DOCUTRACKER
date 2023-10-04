<script>
  import { fetchData, backendAddress } from "../../stores";
  import { navigate } from "svelte-routing";
  import { onMount } from "svelte";

  import Auth from "../entries/auth.svelte";

  const homeAddress = `${backendAddress}index`;
  const homeErrMsg = "";

  let token = localStorage.getItem("remembered") || "";
  let authBind;

  onMount(() => {
    if (token.length === 0) {
      navigate("/");
      return;
    }

    document.title = "DOCUTRACKER | Home";
    authBind.getEndPoint(homeAddress, homeErrMsg, {
      Authorization: `Bearer ${token}`,
    });
  });
</script>

<Auth bind:this={authBind} />
<section>
  <!-- {#if Object.keys($fetchData).length != 0}
    <h1>Currently logged in as:</h1>
    <h2>{$fetchData["email"]}</h2>
    <p>ID: {$fetchData["id"]}, Username: {$fetchData["user_name"]}</p>
  {/if} -->
</section>

<style>
  /* div {
    display: flex;
    justify-content: center;
    align-items: center;
  } */
  section {
    flex: 2;
  }
</style>
