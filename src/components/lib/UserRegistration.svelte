<script lang="ts">
  import { fly, fade } from "svelte/transition";
  import { quintInOut } from "svelte/easing";
  import { blobToBase64 } from "../shared/ImageConverter";
  import {
    registrationExpand,
    handleFetch,
    address,
    dark,
    type Credentials,
    type RegisterBind,
  } from "../../store";

  import Cropper from "svelte-easy-crop";
  import EditIcon from "../icons/EditIcon.svelte";
  import CheckIcon from "../icons/CheckIcon.svelte";
  import Button from "../shared/Button.svelte";
  import Input from "../shared/Input.svelte";
  import UserIcon from "../../assets/user-icon.png";
  import BarLoader from "../shared/BarLoader.svelte";

  let fileData: FileList;
  let base64String: string | null;
  let pixelCrop: { width: number; height: number; x: number; y: number };
  let fileName = "Upload Your Profile";
  let croppedImage: string | null;
  let crop: { x: number; y: number };
  let zoom = 1;

  function handleImage() {
    croppedImage = null;
    zoom = 1;
    crop = { x: 0, y: 0 };

    let files = fileData[0];
    fileName = files.name;
    const reader = new FileReader();

    reader.onload = function (e) {
      if (typeof e.target!.result === "string") {
        base64String = e.target!.result;
      } else {
        console.warn("Event target is an Array Buffer at line 33");
      }
    };

    reader.readAsDataURL(files);
  }

  const createImage = (url: string) =>
    new Promise((resolve, reject) => {
      const image = new Image();
      image.addEventListener("load", () => resolve(image));
      image.addEventListener("error", (error) => reject(error));
      image.setAttribute("crossOrigin", "anonymous");
      image.src = url;
    });

  function getRadianAngle(degreeValue: number) {
    return (degreeValue * Math.PI) / 180;
  }

  export async function getCroppedImg(
    imageSrc: string | null,
    pixelCrop: { width: any; height: any; x: any; y: any },
    rotation = 0
  ): Promise<string> {
    const image = (await createImage(imageSrc!)) as HTMLImageElement;
    const canvas: HTMLCanvasElement = document.createElement("canvas");
    const ctx: CanvasRenderingContext2D = canvas.getContext("2d")!;

    const maxSize = Math.max(image.width, image.height);
    const safeArea = 2 * ((maxSize / 2) * Math.sqrt(2));

    canvas.width = safeArea;
    canvas.height = safeArea;

    ctx.translate(safeArea / 2, safeArea / 2);
    ctx.rotate(getRadianAngle(rotation));
    ctx.translate(-safeArea / 2, -safeArea / 2);

    ctx.drawImage(
      image,
      safeArea / 2 - image.width * 0.5,
      safeArea / 2 - image.height * 0.5
    );
    const data = ctx.getImageData(0, 0, safeArea, safeArea);

    canvas.width = pixelCrop.width;
    canvas.height = pixelCrop.height;

    ctx.putImageData(
      data,
      Math.round(0 - safeArea / 2 + image.width * 0.5 - pixelCrop.x),
      Math.round(0 - safeArea / 2 + image.height * 0.5 - pixelCrop.y)
    );

    return new Promise((resolve) => {
      canvas.toBlob((file) => {
        resolve(URL.createObjectURL(file!));
      }, "image/png");
    });
  }

  export async function getRotatedImage(imageSrc: string, rotation = 0) {
    const image = (await createImage(imageSrc)) as HTMLImageElement;
    const canvas: HTMLCanvasElement = document.createElement("canvas");
    const ctx: CanvasRenderingContext2D = canvas.getContext("2d")!;

    const orientationChanged =
      rotation === 90 ||
      rotation === -90 ||
      rotation === 270 ||
      rotation === -270;
    if (orientationChanged) {
      canvas.width = image.height;
      canvas.height = image.width;
    } else {
      canvas.width = image.width;
      canvas.height = image.height;
    }

    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate((rotation * Math.PI) / 180);
    ctx.drawImage(image, -image.width / 2, -image.height / 2);

    return new Promise((resolve) => {
      canvas.toBlob((file) => {
        resolve(URL.createObjectURL(file!));
      }, "image/webp");
    });
  }

  let submit: HTMLInputElement;
  let isRequest = false;

  let registerUser: Credentials = {
    userImg: "",
    firstName: "",
    middleName: "",
    lastName: "",
  };

  let inputBinds: RegisterBind = {
    firstNameInput: false,
    middleNameInput: false,
    lastNameInput: false,
  };

  const registrationMethod = "POST";
  const registrationAddress = `${address}/registration`;
  let bindForm: HTMLFormElement;

  $: registrationRequest = {
    method: registrationMethod,
    address: registrationAddress,
    credentials: registerUser,
  };

  const handleInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const id = target.id;

    if (id === "First Name") {
      registerUser.firstName = target.value;
    }

    if (id === "Middle Name") {
      registerUser.middleName = target.value;
    }

    if (id === "Last Name") {
      registerUser.lastName = target.value;
    }
  };

  const handleSubmit = async () => {
    const base64String = await blobToBase64(croppedImage);
    registrationRequest.credentials.userImg = base64String;

    isRequest = true;

    try {
      await handleFetch(
        registrationRequest,
        sessionStorage.getItem("remember")
      );
    } catch (error) {
      console.error(error);
      isRequest = false;
    }

    isRequest = false;
    $registrationExpand = false;
  };
</script>

{#if isRequest}
  <BarLoader />
{/if}

<div
  class="full-reg-container"
  class:dark={$dark}
  transition:fade={{ duration: 200, delay: 100 }}
>
  <section
    class:dark={$dark}
    transition:fly={{
      x: 1000,
      delay: 350,
      duration: 1500,
      easing: quintInOut,
    }}
  >
    <div class="cropper-wrapper">
      {#if base64String}
        <!-- svelte-ignore a11y-img-redundant-alt -->
        {#if croppedImage}
          <img
            class="final-user-picture"
            transition:fade={{ duration: 300, delay: 0 }}
            src={croppedImage}
            alt="User Image"
          />
        {:else}
          <Cropper
            image={base64String}
            bind:crop
            bind:zoom
            cropShape="round"
            aspect={1}
            on:cropcomplete={(e) => (pixelCrop = e.detail.pixels)}
          />
        {/if}
      {:else}
        <img
          class="user-icon-wrapper"
          src={UserIcon}
          alt="User Anonymous Icon"
        />
      {/if}
    </div>
    <!-- {#if fileName.length !== 0} -->
    <h3 class:dark={$dark} transition:fade={{ duration: 300, delay: 200 }}>
      {fileName}
    </h3>
    <!-- {/if} -->
    <form bind:this={bindForm} on:submit|preventDefault={handleSubmit}>
      <div class="image-wrapper">
        <label for="image_upload">
          <EditIcon />
        </label>
        <CheckIcon
          on:click={async () => {
            croppedImage = await getCroppedImg(base64String, pixelCrop);
          }}
        />
        <input
          id="image_upload"
          bind:files={fileData}
          on:change={handleImage}
          type="file"
          accept=".jpg, .jpeg, .png"
          required
        />
      </div>
      <div class="first-section">
        <Input
          inputType="text"
          inputName="First Name"
          on:input={handleInput}
          overlap={true}
          dark={$dark}
          bind:focusedInput={inputBinds.firstNameInput}
        />
        <Input
          inputType="text"
          inputName="Middle Name"
          overlap={true}
          on:input={handleInput}
          dark={$dark}
          bind:focusedInput={inputBinds.middleNameInput}
        />
        <Input
          inputType="text"
          inputName="Last Name"
          overlap={true}
          on:input={handleInput}
          dark={$dark}
          bind:focusedInput={inputBinds.lastNameInput}
        />
      </div>
      <input type="submit" bind:this={submit} />
    </form>
    <div class="button-wrapper">
      <Button
        hoverized={$dark ? true : false}
        on:click={() => {
          $registrationExpand = false;
        }}>Close</Button
      >
      <Button hoverized={$dark ? true : false} on:click={() => submit.click()}
        >Save</Button
      >
    </div>
  </section>
</div>

<style>
  div.full-reg-container {
    position: fixed;
    inset: 0;
    z-index: 5;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: flex-end;
    transition: all ease-in-out 500ms;

    & section {
      width: 70%;
      height: 100vh;
      background-color: var(--main-col-5);
      text-align: center;
      transition: all ease-in-out 500ms;
      position: relative;

      & div.cropper-wrapper {
        display: inline-block;
        width: 20rem;
        height: 20rem;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        position: relative;

        & img.final-user-picture {
          width: 20rem;
          height: 20rem;
          border-radius: 50%;
        }

        & img.user-icon-wrapper {
          width: 20rem;
          height: 20rem;
        }
      }

      & h3 {
        margin-bottom: 0.5rem;
        color: var(--main-col-3);
        transition: all ease-in-out 500ms;
      }

      & h3.dark {
        color: var(--background);
      }

      & form {
        margin: auto;
        max-width: 50%;

        & div.image-wrapper {
          & input[type="file"] {
            display: none;
          }
        }

        & input[type="submit"] {
          display: none;
        }
      }

      & div.button-wrapper {
        display: flex;
        column-gap: 0.5rem;
        position: absolute;
        bottom: 1.5rem;
        right: 1.5rem;
        width: 40%;
      }

      & div.button-wrapper > * {
        flex: 1;
      }
    }

    & section.dark {
      background-color: var(--dark-main-col-7);
    }
  }

  div.dark {
    background-color: rgba(45, 53, 75, 0.7);
  }

  @media (max-width: 700px) {
    div.full-reg-container section {
      width: 100%;
    }
  }
</style>
