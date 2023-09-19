<script>
  import { fade } from "svelte/transition";
</script>

<div transition:fade={{ delay: 100, duration: 200 }}>
  <div class="loader" />
</div>

<style>
  div {
    position: absolute;
    inset: 0;

    transition: ease-in-out 500ms;
    opacity: 0.7;
    background-color: white;
    z-index: 4;
  }

  .loader {
    position: relative;
    width: 100%;
    height: 3px;
    background: #ddd;
    transition: ease-in-out 500ms;
    overflow: hidden;
  }

  .loader:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 0;
    background-color: blue;
    animation: progress 1.5s linear infinite;
  }

  @keyframes progress {
    0% {
      width: 0;
      left: 0;
    }

    50% {
      width: 60%;
    }

    100% {
      left: 100%;
    }
  }
</style>
