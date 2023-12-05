<script lang="ts">
  import { onMount, onDestroy } from "svelte";

  import CheckAuthenticity from "../shared/CheckAuthenticity.svelte";
  export let authToken = "";

  type DocumentData = {
    documentName: string;
    documentDescription: string;
    codeData: string;
    regAt: string;
  };

  let allData: DocumentData[] = [
    { documentName: "", documentDescription: "", codeData: "", regAt: "" },
  ];

  export let documentData: DocumentData = {
    documentName: "",
    documentDescription: "",
    codeData: "",
    regAt: "",
  };

  $: {
    if (
      documentData.codeData.length ||
      documentData.documentDescription.length ||
      documentData.documentName.length
    )
      allData.push(documentData);
  }

  $: console.log(documentData);

  onDestroy(() => {
    documentData = {
      documentName: "",
      documentDescription: "",
      codeData: "",
      regAt: "",
    };
  });
</script>

{#each allData as value}
  {#if value.documentName.length && value.documentDescription.length && value.codeData.length}
    <pre>
    {value.documentDescription}
  </pre>
  {/if}
{/each}
<CheckAuthenticity {authToken} on:user></CheckAuthenticity>
<main>Hello From Document Overview</main>
