<script lang="ts">
  import { dark } from "../../store";
  import { fly } from "svelte/transition";
  import {
    type ResponseData,
    type Document,
  } from "../../store";

  import ScanDocument from "../lib/ScanDocument.svelte";
  import RegisterDocument from "../lib/RegisterDocument.svelte";
  import RegisterRoute from "../lib/RegisterRoute.svelte";
  import UnverifiedComp from "./UnverifiedComp.svelte";

  export let shortcutData = "Hello from Shortcut Wrapper";
  export let fullVerified: boolean | undefined = false;
  export let routes: Document = {
    codeData: "",
    documentName: "",
    documentDescription: "",
    documentRegDate: "",
    documentPath: [{ approved: false, name: "" }],
  };


  export let fullname: {
    firstName: string;
    middleName: string;
    lastName: string;
  } = { firstName: "", middleName: "", lastName: "" };
  export let authToken = "";
</script>

<div
  class="shortcut-wrapper"
  class:dark={$dark}
  in:fly={{ x: 1000, duration: 800, delay: 100 }}
  out:fly={{ x: 1000, duration: 800, delay: 100 }}
>
  {#if shortcutData === "Scan Document"}
    {#if fullVerified}
      <ScanDocument {authToken} on:closeShortCut on:documentData></ScanDocument>
    {:else}
      <UnverifiedComp></UnverifiedComp>
    {/if}
  {:else if shortcutData === "Register Document"}
    {#if fullVerified}
      <RegisterDocument {fullname} {routes} {authToken}
      ></RegisterDocument>
    {:else}
      <UnverifiedComp></UnverifiedComp>
    {/if}
  {:else if shortcutData === "Register Route"}
    {#if fullVerified}
      <RegisterRoute {authToken} on:route></RegisterRoute>
    {:else}
      <UnverifiedComp></UnverifiedComp>
    {/if}
    <!-- {:else}
    {shortcutData} -->
  {/if}
</div>

<style>
  div.shortcut-wrapper {
    overflow-y: auto;
    transition: background-color ease-in-out 300ms;
    position: absolute;
    top: 3rem;
    height: calc(100vh - 43.16px);
    background-color: var(--main-col-5);
    width: 100%;
  }

  div.shortcut-wrapper::-webkit-scrollbar {
    width: 0.5rem;
    height: 0.5rem;
  }

  div.shortcut-wrapper::-webkit-scrollbar-track {
    background: var(--main-col-6);
  }

  div.shortcut-wrapper::-webkit-scrollbar-thumb {
    background: var(--main-col-3);
  }

  div.shortcut-wrapper::-webkit-scrollbar-thumb:hover {
    background: var(--scroll-color);
  }

  div.dark {
    background-color: var(--dark-main-col-7);
  }
</style>
