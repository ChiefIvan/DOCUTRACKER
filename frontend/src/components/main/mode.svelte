<script>
  import { beforeUpdate } from "svelte";
  import { expand, dark, openProfile } from "../../stores";

  import SunIcon from "../assets/sunIcon.svelte";
  import MoonIcon from "../assets/moonIcon.svelte";
  import SystemIcon from "../assets/systemIcon.svelte";

  let mode;

  beforeUpdate(() => {
    mode = localStorage.getItem("mode");
    mode !== "System"
      ? mode !== "Dark"
        ? ($dark = false)
        : ($dark = true)
      : !window.matchMedia("(prefers-color-scheme: dark)").matches
      ? ($dark = false)
      : ($dark = true);
  });

  const enableLight = () => {
    mode = localStorage.setItem("mode", "Light");
    $expand = false;
  };

  const enableDark = () => {
    mode = localStorage.setItem("mode", "Dark");
    $expand = false;
  };

  const enableSystem = () => {
    mode = localStorage.setItem("mode", "System");
    $expand = false;
  };

  const modes = [
    { id: 1, modeName: "Light", comp: SunIcon, bind: enableLight },
    { id: 2, modeName: "Dark", comp: MoonIcon, bind: enableDark },
    { id: 3, modeName: "System", comp: SystemIcon, bind: enableSystem },
  ];

  const openModes = () => {
    $openProfile = false;
    $expand = !$expand;
  };
</script>

{#each modes as value (value.id)}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->

  {#if value.modeName === mode}
    <div class="comp-render" on:click|stopPropagation={openModes}>
      <svelte:component this={value.comp} active={true} />
    </div>
  {/if}
{/each}

<div class="comp-wrapper" class:wrapper-expand={$expand} class:dark={$dark}>
  <ul class="mode-wrapper">
    {#each modes as value (value.id)}
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
      <li on:click={value.bind}>
        <svelte:component
          this={value.comp}
          active={value.modeName === mode && true}
        />
        <span class:active={value.modeName === mode && true}
          >{value.modeName}</span
        >
      </li>
    {/each}
  </ul>
</div>

<style>
  .comp-render {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .comp-wrapper {
    display: grid;
    grid-template-rows: 0fr;

    overflow: hidden;
    position: fixed;
    top: 3.5rem;
    right: 3rem;
    z-index: 1;

    transition: all ease-in-out 400ms;
    background-color: #fff;
    box-shadow: 5px 5px 25px lightgray;
    border-radius: var(--size-6);
    box-shadow: 5px 5px 25px var(--main-col-2);

    & ul.mode-wrapper {
      min-height: 0;

      & li {
        display: flex;
        align-items: center;
        column-gap: var(--size-6);
        margin: 0.2rem;
        padding: 0.2rem var(--size-6);
        border-radius: calc(var(--size-6) * 0.8);
        transition: all ease-in-out var(--dur);
        cursor: pointer;

        & span {
          color: var(--main-col-1);
        }

        & span.active {
          color: var(--ico-actv);
        }
      }

      & li:hover {
        background-color: var(--main-col-2);
      }
    }
  }

  div.wrapper-expand {
    grid-template-rows: 1fr;
  }

  div.dark {
    background-color: var(--dark-main-col-5);
    box-shadow: none;
  }
</style>
