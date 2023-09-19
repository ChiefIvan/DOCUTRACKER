<script>
  // @ts-nocheck

  import { afterUpdate } from "svelte";
  import { entryState, resetInput } from "../../stores";

  export let inputName = "";
  export let inputType = "";
  export let inputAutocomplete = "";
  export let inputValue = "";
  export let miniModal = "";
  export let errorColor = "";
  export let inputZ = "";

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
>
  {#if miniModal.length !== 0}
    {#if activeWarning}
      {#if showModal}
        <section>
          {miniModal}
        </section>
      {/if}
      <p
        on:mouseover={() => (showModal = true)}
        on:mouseout={() => (showModal = false)}
      >
        !
      </p>
    {/if}
  {/if}
  <label
    style={`color: ${errorColor}; z-index: ${inputZ}`}
    class:active-slide={inputState}
    class:focus-active={activeFocus}
    for={inputName}>{inputName}</label
  >
  <input
    required
    style={errorColor.length !== 0 && `border-bottom: 1px solid ${errorColor}`}
    id={inputName}
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
  :root {
    --transition: all ease-in-out;
    --entry-color: lightgray;
  }

  div {
    display: flex;
    align-items: center;
    position: relative;
    cursor: text;

    & section {
      position: absolute;
      bottom: 1rem;
      right: -3.6rem;

      background-color: gray;
      color: white;
      width: 10rem;
      font-size: 0.8rem;
      text-align: center;
      padding: 0.8rem;
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

      width: 1.5rem;
      height: 1.5rem;
      background-color: crimson;
      color: white;
      border-radius: 1rem;
      text-align: center;
      font-family: none;
      font-weight: bolder;
      cursor: pointer;
      font-size: 1.3rem;
      user-select: none;
      -webkit-user-select: none;
    }

    & p:hover section {
      display: block;
    }

    & label {
      font-size: 1.2rem;
      user-select: none;
      transition: var(--transition) 250ms;
      padding: 1.1rem;
      color: gray;
      cursor: text;

      position: absolute;
      z-index: -1;
    }

    & label.active-slide {
      font-size: 0.7rem;
      padding: 0 1rem;
      transform: translateY(-1.4rem);
    }

    & label.focus-active {
      color: var(--brdr-actv);
    }

    & input {
      height: 2rem;
      width: 25rem;
      padding: 0 1rem;
      transition: var(--transition) 300ms;
      border: 1px solid transparent;
      border-bottom: 1px solid var(--entry-color);
      outline: none;
      background: transparent;
    }

    & input.focus-active {
      border-bottom: 1px solid var(--brdr-actv);
    }
  }

  div:hover input {
    border-bottom: 1px solid orange;
  }

  div:hover label {
    color: orange;
  }
</style>
