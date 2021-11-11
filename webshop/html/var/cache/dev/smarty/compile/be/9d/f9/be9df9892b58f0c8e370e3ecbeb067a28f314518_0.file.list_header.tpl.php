<?php
/* Smarty version 3.1.39, created on 2021-11-11 13:43:23
  from '/var/www/html/admin776jdno0g/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_618d0feb441e56_64627144',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'be9df9892b58f0c8e370e3ecbeb067a28f314518' => 
    array (
      0 => '/var/www/html/admin776jdno0g/themes/default/template/controllers/attributes_groups/helpers/list/list_header.tpl',
      1 => 1636632028,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_618d0feb441e56_64627144 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_1623200780618d0feb4415f2_48779398', 'leadin');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, "helpers/list/list_header.tpl");
}
/* {block 'leadin'} */
class Block_1623200780618d0feb4415f2_48779398 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'leadin' => 
  array (
    0 => 'Block_1623200780618d0feb4415f2_48779398',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

	<?php echo '<script'; ?>
 type="text/javascript">
		$(document).ready(function() {
			$(location.hash).click();
		});
	<?php echo '</script'; ?>
>
<?php
}
}
/* {/block 'leadin'} */
}
