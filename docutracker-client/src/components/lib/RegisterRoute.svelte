<script lang="ts">
  import {
    showMessage,
    dark,
    handleFetch,
    address,
    type ResponseData,
    type RequestAPI,
  } from "../../store";

  import Input from "../shared/Input.svelte";
  import Button from "../shared/Button.svelte";

  export let authToken = "";

  interface InputBinds {
    [key: string]: boolean;
  }

  let submit: HTMLInputElement;
  let formBind: HTMLFormElement;
  let inputCount = [1];
  let routes: any = { "Route 1": "" };
  let inputBinds: InputBinds = { "Route 1": false };
  let count = 1;

  const handleIncreament = () => {
    count++;
    inputCount = [...inputCount, count];
    routes = { ...routes, [`Route ${count}`]: "" };
    inputBinds = { ...inputBinds, [`Route ${count}`]: false };
  };

  const handleDelete = () => {
    if (count <= 1) {
      $showMessage = { error: "You can't have 0 Routes!" };
      return;
    }

    const lastElement = inputCount.pop();
    delete routes[`Route ${lastElement}`];
    delete inputBinds[`Route ${lastElement}`];
    inputCount = [...inputCount];
    routes = { ...routes };
    inputBinds = { ...inputBinds };
    count--;
  };

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const id = target.id;
    const value = target.value;

    routes[id] = value;
  };

  let nameValue = "";
  let nameBind = false;

  const handleRouteName = (event: Event) => {
    const target = event.target as HTMLInputElement;
    nameValue = target.value;
  };

  let addRoute: RequestAPI = {
    method: "POST",
    address: `${address}/add_route`,
    credentials: {},
  };

  const handleSubmit = async () => {
    addRoute.credentials!.documentPath = routes;
    addRoute.credentials!.routeName = nameValue;

    await handleFetch(addRoute, authToken);

    formBind.reset();
    nameBind = false;
    inputBinds = Object.keys(inputBinds).reduce((acc, key) => {
      acc[key] = false;
      return acc;
    }, {});
  };
</script>

<div class="wrapper" on:submit|preventDefault={handleSubmit}>
  <form bind:this={formBind} class="input-wrapper" autocomplete="off">
    <Input
      inputType="text"
      inputName="Document Name (Associated with this route)"
      overlap={true}
      bind:focusedInput={nameBind}
      dark={$dark}
      on:input={handleRouteName}
    ></Input>
    {#each inputCount as value (value)}
      <svelte:component
        this={Input}
        inputType="text"
        inputName={`Route ${value}`}
        overlap={true}
        bind:focusedInput={inputBinds[`Route ${value}`]}
        dark={$dark}
        on:input={handleInput}
      ></svelte:component>
    {/each}
    <input type="submit" bind:this={submit} />
  </form>
  <div class="button-wrapper">
    <div class="buttons">
      <div class="add-del">
        <Button on:click={handleIncreament}>Add Route</Button>
        <Button on:click={handleDelete}>Delete Route</Button>
      </div>
      <Button on:click={() => submit.click()}>Submit</Button>
    </div>
  </div>
</div>

<style>
  div.wrapper {
    position: relative;
    display: flex;
    gap: 5rem;
    padding: 2rem;

    & form.input-wrapper {
      width: 50%;

      & input[type="submit"] {
        display: none;
      }
    }

    & div.button-wrapper {
      position: fixed;
      bottom: 2rem;
      right: 5rem;
      width: 30%;

      & div.buttons {
        & div.add-del {
          display: flex;
          column-gap: 0.5rem;
        }
      }

      & div.buttons > * {
        margin-top: 0.5rem;
      }
    }
  }
</style>
