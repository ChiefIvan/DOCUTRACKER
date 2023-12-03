<script lang="ts">
  import { Html5Qrcode } from "html5-qrcode";
  import { onMount } from "svelte";

  import Button from "../shared/Button.svelte";

  let scanning = false;

  let html5Qrcode: Html5Qrcode;

  onMount(() => {
    html5Qrcode = new Html5Qrcode("reader");
  });

  function scan() {
    html5Qrcode.start(
      { facingMode: "environment" },
      {
        fps: 10,
        qrbox: { width: 300, height: 300 },
      },
      onScanSuccess,
      onScanFailure
    );
    scanning = true;
  }

  async function stop() {
    await html5Qrcode.stop();
    scanning = false;
  }

  function onScanSuccess(
    decodedText: string,
    decodedResult: { decodedText: string; result: { text: string } }
  ) {
    alert(`Code matched = ${decodedText}`);
    console.log(decodedResult);
  }

  function onScanFailure(error: any) {
    console.warn(`Code scan error = ${error}`);
  }
</script>

<div class="qr-wrapper">
  <div class="scan">
    <div class="container" id="reader"></div>
    {#if scanning}
      <Button on:click={stop}>stop</Button>
    {:else}
      <Button on:click={scan}>start</Button>
    {/if}
  </div>
  <div class="filesystem">
    <!-- <div class="container" id="reader"></div>
    {#if scanning}
      <Button on:click={stop}>stop</Button>
    {:else}
      <Button on:click={scan}>start</Button>
    {/if} -->
  </div>
</div>

<style>
  div.qr-wrapper {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;

    & div.scan {
      & div.container {
        width: 30rem;
        height: 30rem;
      }
    }

    & div.filesystem {
      width: 30rem;
      height: 30rem;
      background-color: red;
    }
  }
</style>
