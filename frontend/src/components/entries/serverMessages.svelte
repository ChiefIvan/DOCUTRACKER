<script>
  import { afterUpdate } from "svelte";
  import { serverResponse } from "../../stores";
  import { fade } from "svelte/transition";

  let key = "";

  afterUpdate(() => {
    key = String(Object.keys($serverResponse));
  });
</script>

{#if key === "error" || key === "success"}
  <div class="server-message">
    <p
      style={key === "error"
        ? "background-color: crimson"
        : "background-color: green"}
    >
      {$serverResponse[key]}
    </p>
  </div>
{/if}

<style>
  div {
    transition: ease-in-out var(--dur);
    position: fixed;
    top: 0;
    z-index: 1;

    width: 100%;
    text-align: center;
    color: var(--bg);

    & p {
      padding: 0.3rem;
    }
  }
</style>
