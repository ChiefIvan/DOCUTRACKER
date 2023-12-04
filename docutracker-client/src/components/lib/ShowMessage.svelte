<script lang="ts">
  import { location, type ResponseData } from "../../store";
  import { fly } from "svelte/transition";

  export let responseMessage: ResponseData = {};
  $: success = responseMessage.success;
  $: error = responseMessage.error;

  $: {
    if (!success) console.warn("success message is empty");
    if (!error) console.warn("error message is empty");
  }

  type Duration = {
    y?: number;
    x?: number;
    duration: number;
  };

  let isInside = false;
  let transition: Duration = { y: -30, duration: 300 };

  $: if (
    "/dashboard" ||
    $location === "/history" ||
    $location === "/notifications" ||
    $location === "/analytics" ||
    $location === "/document/overview"
  ) {
    isInside = true;
    transition = { x: 200, duration: 300 };
  }
</script>

<div
  class="response-message"
  class:isInside
  class:success={success && true}
  class:error={error && true}
  in:fly={transition}
  out:fly={transition}
>
  <p class="message">{success ? success : error}</p>
</div>

<style>
  div.response-message {
    position: fixed;
    top: 2.5rem;
    z-index: 2;
    padding: 0.4rem 0;
    width: 100%;
    text-align: center;

    & p.message {
      color: var(--background);
      font-weight: 700;
    }
  }

  div.isInside {
    border-radius: 0.5rem;
    top: 4rem;
    right: 1rem;
    z-index: 3;
    width: 30%;
    padding: 1rem;

    & p.message {
      color: var(--background);
      font-weight: 700;
    }
  }

  div.success {
    background-color: #008000;
  }

  div.error {
    background-color: var(--forground-color);
  }
</style>
