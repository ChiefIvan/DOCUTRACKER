<script>
  // @ts-nocheck

  import { afterUpdate } from "svelte";
  import { entryState, resetInput } from "../../stores";
  import { fade } from "svelte/transition";

  export let inputName = "";
  export let inputType = "";
  export let inputAutocomplete = "";
  export let inputValue = "";
  export let miniModal = "";
  export let inputZ = "";
  export let inputSize = "";
  export let errorColor = false;

  let activeFocus = false;
  let inputState = false;
  let activeWarning = false;
  let showModal = false;

  afterUpdate(() => {
    if ($entryState) {
      if (inputValue.length === 0) {
        inputState = false;
      }
    }
  });

  const handleOnfocus = (/** @type {any} */ e) => {
    inputState = true;
    activeFocus = true;
    $entryState = false;
  };

  const handleOfffocus = (
    /** @type {{ target: { value: any; }; }} */ event
  ) => {
    activeFocus = false;

    if (event.target.value) {
      return;
    }

    inputState = false;
  };
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-mouse-events-have-key-events -->
<div
  on:mouseover={() => (activeWarning = true)}
  on:mouseleave={() => (activeWarning = false)}
  style={`width: ${inputSize};`}
>
  {#if miniModal.length !== 0}
    {#if activeWarning}
      {#if showModal}
        <section transition:fade={{ delay: 100, duration: 80 }}>
          {miniModal}
        </section>
      {/if}
      <p
        on:mouseover={() => (showModal = true)}
        on:mouseout={() => (showModal = false)}
        transition:fade={{ delay: 100, duration: 80 }}
      >
        !
      </p>
    {/if}
  {/if}
  <label
    style={`color: ${errorColor}; z-index: ${inputZ}`}
    class:active-slide={inputState}
    class:focus-active={activeFocus}
    class:error-active={errorColor}
    for={inputName}>{inputName}</label
  >
  <input
    required
    style={`border-bottom: 1px solid ${
      errorColor.length !== 0 && errorColor
    }; width: ${inputSize.length !== 0 && inputSize};`}
    id={inputName}
    class:error-active={errorColor}
    class:focus-active={activeFocus}
    type={inputType}
    autocomplete={inputAutocomplete}
    value={inputValue}
    bind:this={$resetInput}
    on:focus={handleOnfocus}
    on:blur={handleOfffocus}
    on:input
  />
</div>

<style>
  div {
    display: flex;
    align-items: center;
    position: relative;
    cursor: text;

    & section {
      position: absolute;
      bottom: 0.5rem;
      right: -3.6rem;

      background-color: var(--main-col-1);
      color: var(--bg);
      width: 10rem;
      font-size: 0.8rem;
      text-align: center;
      padding: 0.5rem;
      padding-bottom: 1.5rem;
      margin-bottom: 1.5rem;
      clip-path: polygon(
        100% 0,
        100% 87%,
        61% 88%,
        52% 100%,
        41% 88%,
        0 87%,
        0 0
      );
    }

    & p {
      position: absolute;
      top: 0;
      right: 0.5rem;
      z-index: 2;

      width: 1.3rem;
      height: 1.3rem;
      background-color: var(--for-col);
      color: var(--bg);
      border-radius: 1rem;
      text-align: center;
      font-family: none;
      font-weight: bolder;
      cursor: pointer;
      font-size: 1.1rem;
      user-select: none;
      -webkit-user-select: none;
    }

    & p:hover section {
      display: block;
    }

    & label {
      font-size: 1.05rem;
      user-select: none;
      transition: ease-in-out calc(var(--dur) / 2);
      padding: 1.1rem;
      color: var(--main-col-1);
      cursor: text;

      position: absolute;
      z-index: -1;
    }

    & label.active-slide {
      font-size: 0.6rem;
      padding: 0 1rem;
      transform: translateY(-1.22rem);
    }

    & label.focus-active {
      color: var(--brdr-actv);
    }

    & label.error-active {
      color: var(--for-col);
    }

    & input {
      height: 1.6rem;
      width: var(--size-4);
      padding: 0 1rem;
      transition: ease-in-out calc(var(--dur) / 2);
      border: 1px solid var(--tran-color);
      border-bottom: 1px solid var(--main-col-2);
      outline: none;
      background: var(--tran-color);
    }

    & input.focus-active {
      border-bottom: 1px solid var(--brdr-actv);
    }

    & input.error-active {
      border-bottom: 1px solid var(--for-col);
    }
  }

  div:hover input {
    border-bottom: 1px solid var(--brdr-hovr);
  }

  div:hover label {
    color: var(--brdr-hovr);
  }
</style>
