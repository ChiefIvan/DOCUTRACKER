<script lang="ts">
  import { type ResponseData } from "../../store";
  import { fly } from "svelte/transition";
  // import {  } from "svelte/easing";

  export let responseMessage: ResponseData = {};
  $: success = responseMessage.success;
  $: error = responseMessage.error;

  $: {
    if (!success) console.warn("success message is empty");
    if (!error) console.warn("error message is empty");
  }
</script>

<div
  class="response-message"
  class:success={success && true}
  class:error={error && true}
  in:fly={{ y: -30, duration: 300 }}
  out:fly={{ y: -30, duration: 300 }}
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

  div.success {
    background-color: #008000;
  }

  div.error {
    background-color: var(--forground-color);
  }

  /* @media {

  } */
</style>
