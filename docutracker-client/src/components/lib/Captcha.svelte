<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import {
    address,
    handleFetch,
    type RequestAPI,
    type ResponseData,
    type Credentials,
  } from "../../store";
  import { fade } from "svelte/transition";

  import Input from "../shared/Input.svelte";
  import Button from "../shared/Button.svelte";

  type EventDispatcher = (eventname: string, value: boolean) => void;

  export let captchaImage: string = "";

  const captchaAddress: string = `${address}/captcha`;
  const method: string = "POST";
  const dispatch: EventDispatcher = createEventDispatcher();

  let bindForm: HTMLFormElement;

  let credentials: Credentials = {
    captcha: "",
    captchaID: "",
  };

  const request: RequestAPI = {
    method: method,
    address: captchaAddress,
    credentials: credentials,
  };

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;

    credentials.captcha = target.value;
  };

  const handleSubmit = async () => {
    bindForm.reset();

    credentials.captchaID = sessionStorage.getItem("captchaID");
    const response: ResponseData = await handleFetch(request);

    if (response.captchaPOSTValue === undefined) {
      console.error("Captcha POST Value is Undefined");
      return;
    }

    if (!response.captchaPOSTValue) {
      console.warn("Captcha POST Value is False");
    }

    dispatch("dispatch", response.captchaPOSTValue);
  };
</script>

<div transition:fade class="captcha-wrapper">
  <form
    bind:this={bindForm}
    on:submit|preventDefault={handleSubmit}
    autocomplete="off"
  >
    <img
      class="captcha-image"
      src={`data:image/jpeg;base64,${captchaImage}`}
      alt="Captcha"
    />
    <Input
      inputType="text"
      inputName="Captcha"
      on:input={handleInput}
      overlap={true}
    />
    <Button>Verify</Button>
  </form>
</div>

<style>
  div.captcha-wrapper {
    position: absolute;
    inset: 0;
    z-index: 4;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(84, 84, 84, 0.6);
    padding: 1rem;
    min-width: 15rem;

    & form {
      background-color: var(--background);
      box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.1);
      border-radius: 1rem;
      padding: 0.5rem;

      & img.captcha-image {
        max-width: -webkit-fill-available;
      }
    }
  }
</style>
