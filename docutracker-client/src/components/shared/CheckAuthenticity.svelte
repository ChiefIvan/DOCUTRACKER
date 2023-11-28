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
