// For more info, see https://github.com/storybookjs/eslint-plugin-storybook#configuration-flat-config-format
import storybook from 'eslint-plugin-storybook';

import prettier from 'eslint-config-prettier';
import path from 'node:path';
import { includeIgnoreFile } from '@eslint/compat';
import js from '@eslint/js';
import svelte from 'eslint-plugin-svelte';
import { defineConfig } from 'eslint/config';
import globals from 'globals';
import ts from 'typescript-eslint';
import svelteConfig from './svelte.config.js';
import importPlugin from 'eslint-plugin-import';
import pluginQuery from '@tanstack/eslint-plugin-query';

const gitignorePath = path.resolve(import.meta.dirname, '.gitignore');

export default defineConfig(
	...storybook.configs['flat/recommended'],
	...pluginQuery.configs['flat/recommended-strict'],
	includeIgnoreFile(gitignorePath),
	js.configs.recommended,
	ts.configs.recommended,
	svelte.configs.recommended,
	prettier,
	svelte.configs.prettier,
	{
		languageOptions: { globals: { ...globals.browser, ...globals.node } },
		rules: {
			'no-undef': 'off',
			'svelte/no-navigation-without-resolve': 'off'
		}
	},
	{
		files: ['**/*.svelte', '**/*.svelte.ts', '**/*.svelte.js'],
		languageOptions: {
			parserOptions: {
				projectService: true,
				extraFileExtensions: ['.svelte'],
				parser: ts.parser,
				svelteConfig
			}
		}
	},
	// Unidirectional codebase + cross-feature import restrictions
	{
		plugins: {
			import: importPlugin
		},
		rules: {
			'import/no-restricted-paths': [
				'error',
				{
					zones: [
						// 單向資料流：routes（app layer）不能被 features 引入
						{
							target: './src/features',
							from: './src/routes'
						},

						// 單向資料流：shared 模組不能引入 features 或 routes
						{
							target: [
								'./src/components',
								'./src/hooks',
								'./src/lib',
								'./src/types',
								'./src/utils'
							],
							from: ['./src/features', './src/routes']
						}
					]
				}
			]
		}
	}
);
