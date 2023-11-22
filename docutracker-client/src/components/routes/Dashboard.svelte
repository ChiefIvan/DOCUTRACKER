<script lang="ts">
  import {
    handleFetch,
    address,
    dark,
    registrationExpand,
    type RequestAPI,
    type ResponseData,
  } from "../../store";
  import { navigate } from "svelte-routing";
  import { createEventDispatcher } from "svelte";
  import { onMount, afterUpdate } from "svelte";

  import UserRegistration from "../lib/UserRegistration.svelte";

  const dispatch = createEventDispatcher();
  const indexAddress = `${address}/index`;
  const indexMethod = "GET";
  const streamAddress = `${address}/user_credentials_updates`;
  const authToken = sessionStorage.getItem("remember") || "";

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

  const streamRequest: RequestAPI = {
    method: indexMethod,
    address: streamAddress,
  };

  let intervalId: string | number | NodeJS.Timeout | undefined;

  afterUpdate(async () => {
    if (intervalId) {
      clearInterval(intervalId);
    }

    intervalId = setInterval(async () => {
      const response: ResponseData = await handleFetch(
        streamRequest,
        authToken
      );
    }, 5000);
  });

  onMount(async () => {
    await fetchDataAndDispatch();
    await fetchEventSourceAndLog();
  });

  const handleAbort = () => {};
</script>

<main class:dark={$dark}>
  <!--  -->
</main>
<div class="sample" />
<div class="sample" />

{#if $registrationExpand}
  <UserRegistration />
{/if}

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

  div.sample {
    height: 100vh;
  }
</style>
