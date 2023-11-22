<script lang="ts">
  import { tooltip } from "./Tooltip";
  import { fade } from "svelte/transition";

  export let inputType = "text";
  export let inputName = "text";
  export let tooltipContent = "";
  export let showWarningMark = false;
  export let focusedInput = false;
  export let overlap = false;
  export let verifiedEntry = true;
  export let dark = false;

  const handleFocus = () => {
    focusedInput = true;
  };

  const handleBlur = (event: FocusEvent) => {
    const target = event.target as HTMLInputElement;
    if (target.value) {
      return;
    }

    focusedInput = false;
  };

  $: showWarningMark = !verifiedEntry ? true : false;
</script>

<div class="input-container" class:increase-overlap={overlap}>
  <label
    class="input-label"
    class:slide={focusedInput}
    class:increase-overlap={overlap}
    class:not-verified={!verifiedEntry}
    class:dark
    for={inputName}>{inputName}</label
  >
  <input
    on:focus={handleFocus}
    on:blur={handleBlur}
    on:input
    class:dark
    class="input"
    class:not-verified={!verifiedEntry}
    type={inputType}
    name={inputName}
    id={inputName}
    required
  />
  {#if tooltipContent.length !== 0}
    {#if showWarningMark}
      <div
        transition:fade={{ duration: 300, delay: 300 }}
        use:tooltip={{
          content: tooltipContent,
          animation: "perspective-subtle",
          theme: "tooltip",
        }}
        class="warning-mark-container"
      >
        <span class="warning-mark">!</span>
      </div>
    {/if}
  {/if}
</div>

<style>
  /* :global(.tippy-box[data-theme="tooltip"]) {
    background-color: var(--forground-color);
  }

  :global(.tippy-arrow) {
    color: var(--forground-color);
  } */

  :global(.tippy-content) {
    font-size: 0.8rem;
  }

  div.input-container {
    position: relative;
    margin: 1rem 0;

    & label.input-label {
      position: absolute;
      font-size: 1.2rem;
      transition: all ease-in-out 300ms;
      padding: 0 0.5rem;
      color: var(--scroll-color);
      z-index: -1;
      user-select: none;
      -webkit-user-select: none;
    }

    & label.slide {
      transform: translateY(-0.9rem);
      font-size: 0.7rem;
    }

    & label.not-verified {
      color: var(--forground-color);
    }

    & label.dark {
      color: var(--background);
    }

    & input.input {
      padding: 0 0.5rem;
      width: 100%;
      height: 1.8rem;
      font-size: 1.1rem;
      background-color: transparent;
      border: 1px solid transparent;
      border-bottom: 1px solid var(--main-col-2);
      transition: all ease-in-out 300ms;
      outline: none;
    }

    & input.not-verified {
      border-bottom-color: var(--forground-color);
    }

    & input.dark {
      border-bottom-color: var(--input-color);
    }

    & div.warning-mark-container {
      position: absolute;
      cursor: pointer;
      bottom: 0;
      top: 0;
      right: 0;
      background-color: var(--forground-color);
      color: var(--background);
      font-family: Arial, Helvetica, sans-serif;
      text-align: center;
      width: 1.4rem;
      height: 1.4rem;
      border-radius: 50%;

      & span.warning-mark {
        font-size: 1rem;
        font-weight: 900;
        user-select: none;
        -webkit-user-select: none;
      }
    }
  }

  div.increase-overlap {
    z-index: 0;
  }

  div:hover input.input {
    border-bottom-color: var(--border-hover-color) !important;
  }

  div:hover label.input-label {
    color: var(--border-hover-color) !important;
  }
</style>
