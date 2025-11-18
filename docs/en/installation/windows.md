# Installing ConTeXt on Windows 64-bit

**Installation guide for ConTeXt Standalone (MkIV) on Windows 64-bit**

> **IMPORTANT NOTE**: This guide is for installing ConTeXt MkIV (classic standalone version). For the latest version, consider installing [ConTeXt LMTX](https://wiki.contextgarden.net/Installation).

## Overview

ConTeXt Standalone is a complete, up-to-date ConTeXt distribution that can be installed and upgraded efficiently. It can coexist in parallel with other existing TeX installations, such as MiKTeX, TeXLive, etc.

### Advantages of ConTeXt Standalone

- **Continuous updates**: Unlike TeXLive (updated annually), Standalone is updated continuously
- **Non-interfering**: Does not modify your PATH or system variables globally
- **Portable**: Can be moved between directories or computers
- **Multiple instances**: Allows having several versions installed simultaneously
- **Self-contained**: Does not interfere with other installed TeX distributions

### What's Included

- ConTeXt MkIV (LuaTeX engine)
- Free fonts (approximately 200MB)
- rsync binaries for Windows
- Automatic update scripts

### What's NOT Included

- LaTeX and its packages
- ConTeXt MkII (old version)

## Requirements

### System

- Windows 7 or higher
- 64-bit architecture
- Approximately 300MB of disk space
- Internet connection (for initial download and updates)

### Optional Programs

The following programs are not required to run ConTeXt, but add extra functionality:

- **curl**: For including remote content
- **ghostscript**: For converting PostScript images to PDF
- **graphicsmagick** (convert): For converting GIF and TIFF images
- **inkscape**: For converting SVG and compressed SVG
- **mupdf** (mudraw): For converting PDF to PNG (used for ePub covers)
- **pstoedit**: For converting PostScript to MetaPost outlines
- **zint**: For providing barcodes
- **zip** or **7zip**: For EPUB generation

## Installation

### Step 1: Choose Installation Directory

Choose a directory where you want to install ConTeXt. **Important recommendations**:

✅ **Recommended**:
- `C:\context`
- `C:\Programs\context`
- `C:\tools\context`

❌ **Avoid**:
- Paths with spaces: `C:\Program Files\context`
- Very long paths
- Paths with uppercase letters: `C:\CONTEXT` or `C:\Temp`

> **Why?** rsync sometimes has problems with paths containing uppercase letters or spaces. Additionally, due to Windows's 8.3 filename conventions, very long directory names can cause problems.

### Step 2: Download Installation Files

1. Download the installation file for Windows 64-bit:
   - [context-setup-win64.zip](http://minimals.contextgarden.net/setup/context-setup-win64.zip)

2. Extract the contents to your chosen directory (e.g., `C:\context`)

### Step 3: Run Installation

1. Open **Command Prompt** (`cmd.exe`)
   - Press `Win + R`
   - Type `cmd` and press Enter

2. Navigate to the installation directory:
   ```cmd
   cd C:\context
   ```

3. Run the installation script:
   ```cmd
   first-setup.bat
   ```

   **This step takes a long time** (can take 10-30 minutes depending on your connection), so grab a coffee! ☕

### Installation Options

#### Install stable version (instead of beta)

By default, the suite installs the beta version of ConTeXt. To install the stable version:

```cmd
first-setup.bat --context=latest
```

#### Install all third-party modules

By default, the suite does not install modules. To install all available modules:

```cmd
first-setup.bat --modules=all
```

#### Complete installation with modules

For a complete installation with all modules:

```cmd
first-setup.bat --context=latest --modules=all
```

## Proxy Settings (if needed)

If you are behind a proxy server, you need to inform rsync of the details.

### Method 1: Temporary variable

In Command Prompt, before running `first-setup.bat`:

```cmd
set RSYNC_PROXY=username:password@proxyhost:port
```

Replace:
- `username`: your proxy username
- `password`: your proxy password
- `proxyhost`: proxy server address
- `port`: proxy port (usually 8080 or 3128)

### Method 2: Permanent variable

To permanently set the environment variable:

1. Right-click on "My Computer" or "This PC"
2. Select "Properties"
3. Click on "Advanced system settings"
4. Click on "Environment Variables"
5. Add new system variable:
   - Name: `RSYNC_PROXY`
   - Value: `username:password@proxyhost:port`

### Firewall Issues

If port 873 is blocked by the firewall, but port 22 (SSH) is open:

```cmd
set RSYNC_CONNECT_PROG=ssh tunnelhost nc %H 873
```

Where `tunnelhost` is a machine outside the firewall on which you have SSH access.

## Using ConTeXt

ConTeXt Standalone does not interfere with the system because it does not add anything to your `PATH` or set system variables. This means you need to initialize it before use.

### Basic Usage in Command Prompt

Before running ConTeXt, you need to execute `setuptex.bat`:

```cmd
C:\context\tex\setuptex.bat
```

After that, you can use ConTeXt normally:

```cmd
context --version
context my-document.tex
```

### Create Permanent Shortcut

To avoid having to type the path to `setuptex.bat` every time, you can create a shortcut:

1. Right-click on Desktop
2. Select "New" → "Shortcut"
3. In the location field, type:
   ```
   C:\WINDOWS\System32\cmd.exe /k C:\context\tex\setuptex.bat
   ```
   (Adjust `C:\context` to your installation directory)
4. Name the shortcut, for example: "ConTeXt Shell"

Now, clicking this shortcut will open a Command Prompt with ConTeXt already configured!

### Verify Installation

To verify everything is working:

```cmd
C:\context\tex\setuptex.bat
context --version
```

You should see information about the installed ConTeXt version.

## Using ConTeXt with Cygwin

If you use Cygwin, you can run ConTeXt within it:

1. Run `setuptex.bat` in Windows Command Prompt
2. In the same prompt, enter Cygwin by running `cygwin.bat` (in your Cygwin installation directory)
3. In the Cygwin prompt, run: `context.cmd test.tex`

> **Note**: The `.cmd` extension is required in Cygwin.

## Updating ConTeXt

To update your ConTeXt installation:

1. Open Command Prompt
2. Navigate to the installation directory:
   ```cmd
   cd C:\context
   ```
3. Run the installation script again:
   ```cmd
   first-setup.bat
   ```

### Update while keeping installed modules

To update and keep already installed modules:

```cmd
first-setup.bat --keep
```

### Update and install specific modules

```cmd
first-setup.bat --modules=t-letter,t-mathsets
```

## Uninstallation

ConTeXt Standalone does not modify anything outside its installation folder. To uninstall:

1. Simply **delete the installation directory** (e.g., `C:\context`)
2. If you created shortcuts, delete them too

Done! No additional cleanup needed.

## Installing Third-Party Modules

ConTeXt suite only comes with Taco's t-bib module. To install additional modules:

### Install specific module

To install Wolfgang's t-letter module:

```cmd
first-setup.bat --modules=t-letter
```

### Install multiple modules

To install more than one module, separate them with commas:

```cmd
first-setup.bat --modules=t-letter,t-mathsets
```

### Install all modules

To install all extra modules at once:

```cmd
first-setup.bat --modules=all
```

## Reverting to Older Version

If for some reason you want to revert to an older version:

```cmd
first-setup.bat --context=date
```

Where `date` is the date of one of the stable ConTeXt releases. The complete list of old releases available is at: http://minimals.contextgarden.net/setup/

## Moving the Installation

The ConTeXt installation tree is **portable** and can be moved between directories or machines.

To move the installation:

1. Copy the complete directory to the new location
2. In the new location, clear the cache:
   ```cmd
   mtxrun --generate
   ```

This regenerates the cache (`./tex/texmf-cache/luatex-cache`).

## Remaking Formats

Normally, the update script creates formats automatically. If for some reason you need to recreate them:

### For MKIV format (LuaTeX)

```cmd
mtxrun --generate
context --make
```

## Troubleshooting

### Problem: rsync has issues with paths

**Symptoms**: Errors during installation related to paths.

**Solution**:
- Reinstall in a path entirely in lowercase, without spaces
- Example: `C:\context` instead of `C:\Context` or `C:\Program Files\context`

### Problem: Errors with 8-character directory names

**Symptoms**: Missing file warnings containing Windows-created 8-character directory names (e.g., `C:\CONTEX~1\tex`).

**Solution**:
- Use a short directory name (8 characters or less)
- Example: `C:\ctx` or `C:\context`

### Problem: rsync timeout behind firewall

**Symptoms**: Timeout during download.

**Solution**:
- Open port 873 for outgoing TCP connections in the firewall
- Or use the SSH tunneling method (see Proxy section above)

### Problem: Engine mismatch after update

**Symptoms**: Error message like:
```
engine mismatch (luv: This is LuaTeX, Version beta-<version>...)
```

**Solution**:
1. Go to `C:\context\tex\texmf-win64\bin`
2. Make sure `luatex.exe` and `texlua.exe` have the same date
3. Delete the `luatex.dll` file
4. Run `context --make` again

### Problem: ConTeXt not found after installation

**Symptoms**: `context` command is not recognized.

**Solution**:
- Run `setuptex.bat` before using ConTeXt
- Or use the shortcut created in the "Create Permanent Shortcut" section

## Integrating with Editors

To use ConTeXt with your favorite editor:

### Method 1: Via Terminal

1. Open Command Prompt
2. Run `setuptex.bat`
3. Start the editor from the same prompt

### Method 2: Configure Editor PATH

Add `C:\context\tex\texmf-win64\bin` to the PATH that the editor searches. Details vary depending on the editor.

See [Text Editors](../text-editors.md) for specific integration instructions with various editors.

## Using with ConTeXt Academic Press

After installing ConTeXt Standalone, you can use it with the ConTeXt Academic Press framework:

1. Make sure ConTeXt is installed and working
2. Navigate to your CAP project directory
3. Run ConTeXt's `setuptex.bat`
4. Use the CAP CLI normally:
   ```cmd
   python cap.py build
   ```

## Additional Resources

- [ConTeXt Wiki](https://wiki.contextgarden.net)
- [ConTeXt Garden](http://www.contextgarden.net)
- [Mailing list](https://mailman.ntg.nl/mailman/listinfo/ntg-context)
- [Source code browser](http://source.contextgarden.net)

## Next Steps

After successfully installing ConTeXt:

1. Read the [Getting Started Guide](../getting-started.md)
2. Explore the [Design System](../design-system.md)
3. Create your first project with ConTeXt Academic Press
4. Consult the [Components Reference](../components-reference.md)

---

**Documentation updated**: 2025-01-18
**Based on**: ConTeXt Standalone Wiki
