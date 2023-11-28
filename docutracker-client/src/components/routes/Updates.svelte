<script lang="ts">
  import {
    handleFetch,
    address,
    dark,
    type RequestAPI,
    type ResponseData,
  } from "../../store";
  import { navigate } from "svelte-routing";
  import { createEventDispatcher } from "svelte";
  import { onMount } from "svelte";

  export let authToken: string;

  const dispatch = createEventDispatcher();
  const indexAddress = `${address}/index`;
  const indexMethod = "GET";

  const authRequest: RequestAPI = {
    method: indexMethod,
    address: indexAddress,
  };

  async function fetchDataAndDispatch() {
    if (!authToken.length) {
      console.warn("Auth Token is empty");
      navigate("/auth/login");
      return;
    }

    try {
      const response: ResponseData = await handleFetch(authRequest, authToken);
      dispatch("user", response);
    } catch (error) {
      navigate("/auth/login");
      console.error(error);
    }
  }

  async function fetchEventSourceAndLog() {
    if (!authToken.length) {
      console.warn("Auth Token is empty");
      navigate("/auth/login");
      return;
    }
  }

  onMount(async () => {
    await fetchDataAndDispatch();
    await fetchEventSourceAndLog();
  });
</script>

<main class:dark={$dark}>
  <h1>Hello From Updates</h1>
</main>

<style>
  /* main {
    background-color: var(--header-color);
    text-align: center;
    font-size: 10rem;
    line-height: 60vh;
    height: 60vh;
    transition: background-color ease-in-out 400ms;
  }

  main.dark {
    background-color: var(--dark-main-col-6);
  } */

  /* div.sample {
    height: 100vh;
  } */
</style>
