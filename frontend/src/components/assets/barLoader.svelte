<script>
  import { fade } from "svelte/transition";
</script>

<div transition:fade={{ delay: 200, duration: 300 }}>
  <div class="loader" />
</div>

<style>
  div {
    position: absolute;
    inset: 0;

    transition: ease-in-out var(--dur);
    background-color: rgba(255, 255, 255, 0.8);
    z-index: 4;
  }

  .loader {
    position: relative;
    width: 100%;
    height: 3px;
    background: var(--brdr);
    transition: ease-in-out var(--dur);
    overflow: hidden;
  }

  .loader::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 50%;
    background-color: var(--brdr-actv);
    animation: progress 1500ms linear infinite;
  }

  @keyframes progress {
    0% {
      left: -50%;
    }
    50% {
      width: 50%;
    }
    100% {
      left: 120%;
    }
  }
</style>
