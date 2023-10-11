<script>
  import { fetchData, backendAddress, dark } from "../../stores";
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
<section class:dark={$dark}>
  <!-- {#if Object.keys($fetchData).length != 0}
    <h1>Currently logged in as:</h1>
    <h2>{$fetchData["email"]}</h2>
    <p>ID: {$fetchData["id"]}, Username: {$fetchData["user_name"]}</p>
  {/if} -->
  <div class="status-wrapper">
    <h1>Status</h1>
  </div>
  <div class="another" class:dark={$dark} />
  <div class="another" class:dark={$dark} />
</section>

<style>
  /* div {
    display: flex;
    justify-content: center;
    align-items: center;
  } */
  section {
    flex: 2;
    background-color: var(--main-col-6);
    transition: all ease-in-out var(--dur2);

    & div.status-wrapper {
      min-height: 30rem;
      text-align: center;

      & h1 {
        font-size: 10rem;
        line-height: 30rem;
        color: var(--main-col-1);
      }
    }

    & div.another {
      height: 100vh;
      background-color: var(--bg);
    }

    & div.dark {
      background-color: var(--dark-main-col-6);
    }
  }

  section.dark {
    background-color: var(--dark-main-col-2);
  }
</style>
